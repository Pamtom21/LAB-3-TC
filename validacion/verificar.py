"""Verificación reproducible de la GLC: biblioteca estándar de Python 3.10+."""
from pathlib import Path
from copy import deepcopy
import json
import re

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT/'validacion/gramatica.json').read_text(encoding='utf-8'))
BASE = DATA['producciones']
EXT = deepcopy(BASE)
EXT.update(DATA['extension']['producciones'])
EXT['<instruccion>'].append(DATA['extension']['alternativa_instruccion'])
RESERVED = {'Begin', 'End', 'Programa', 'salida'}

def lex(source, extended=False):
    reserved = RESERVED | ({'entero','real'} if extended else set())
    result, i = [], 0
    while i < len(source):
        c=source[i]
        if c.isspace():
            i+=1; continue
        if source.startswith('/*',i):
            end=source.find('*/',i+2)
            if end<0: raise ValueError('Comentario sin cierre')
            i=end+2; continue
        if c.isalpha():
            end=i+1
            while end<len(source) and (source[end].isalpha() or source[end] in '0123456789_'):
                end+=1
            word=source[i:end]
            result.append((word if word in reserved else 'ID',word)); i=end; continue
        if c in '0123456789':
            match=re.match(r'[0-9]+(?:\.[0-9]+)?',source[i:])
            number=match.group()
            result.append(('NUM',number)); i+=len(number); continue
        if c in '=+-*/%#':
            result.append((c,c)); i+=1; continue
        raise ValueError(f'Carácter no admitido en posición {i}: {c!r}')
    return result

def earley(tokens, grammar, start):
    """Reconocedor general de GLC; no codifica las formas de instrucción."""
    types=[t[0] for t in tokens]
    chart=[set() for _ in range(len(types)+1)]
    chart[0].add(('@inicio',(start,),0,0))
    for pos in range(len(chart)):
        changed=True
        while changed:
            changed=False
            for lhs,rhs,dot,origin in list(chart[pos]):
                if dot<len(rhs):
                    symbol=rhs[dot]
                    if symbol in grammar:
                        for alternative in grammar[symbol]:
                            item=(symbol,tuple(alternative),0,pos)
                            if item not in chart[pos]: chart[pos].add(item); changed=True
                    elif pos<len(types) and symbol==types[pos]:
                        chart[pos+1].add((lhs,rhs,dot+1,origin))
                else:
                    for plhs,prhs,pdot,porigin in list(chart[origin]):
                        if pdot<len(prhs) and prhs[pdot]==lhs:
                            item=(plhs,prhs,pdot+1,porigin)
                            if item not in chart[pos]: chart[pos].add(item); changed=True
    return ('@inicio',(start,),1,0) in chart[-1]

def accepts(source, start='<instruccion>', extended=False):
    try: return earley(lex(source,extended),EXT if extended else BASE,start)
    except ValueError: return False

def derive(spec, grammar):
    tree={'symbol':'<instruccion>'}
    frontier=[tree]
    for lhs,choice in spec['pasos']:
        idx=next(i for i,n in enumerate(frontier) if n['symbol'] in grammar)
        node=frontier[idx]
        assert node['symbol']==lhs, 'Paso no es por la izquierda'
        rhs=grammar[lhs][choice]
        node['children']=[{'symbol':s} for s in rhs]
        frontier[idx:idx+1]=node['children']
    assert all(n['symbol'] not in grammar for n in frontier), 'Derivación incompleta'
    scanned=lex(' '.join(spec['lexemas']),grammar is EXT)
    assert [n['symbol'] for n in frontier]==[t[0] for t in scanned]
    assert [t[1] for t in scanned]==spec['lexemas']
    for node,(_,word) in zip(frontier,scanned): node['lexeme']=word
    def check(node):
        if 'children' in node:
            assert [n['symbol'] for n in node['children']] in grammar[node['symbol']]
            for child in node['children']: check(child)
    check(tree)
    return tree

def main():
    rows=[]
    def check(name, condition):
        rows.append(('OK' if condition else 'FALLO')+' | '+name)
        if not condition:
            (ROOT/'evidencias/validacion.txt').write_text('\n'.join(rows)+'\n',encoding='utf-8')
            raise AssertionError(name)

    for name,g,sigma in [('G',BASE,set(DATA['terminales'])),("G'",EXT,set(DATA['terminales']+DATA['extension']['terminales']))]:
        symbols={s for alts in g.values() for rhs in alts for s in rhs}
        check(name+': todos los símbolos declarados',symbols<=set(g)|sigma)
        check(name+': V y Sigma disjuntos',not set(g)&sigma)
        check(name+': terminales declarados utilizados',symbols-set(g)==sigma)
        reachable={DATA['inicio']}
        while True:
            more=reachable|{s for n in reachable for rhs in g[n] for s in rhs if s in g}
            if more==reachable: break
            reachable=more
        check(name+': no terminales alcanzables',reachable==set(g))
        productive=set()
        while True:
            more=productive|{n for n,alts in g.items() if any(all(s not in g or s in productive for s in rhs) for rhs in alts)}
            if more==productive: break
            productive=more
        check(name+': no terminales productivos',productive==set(g))

    text=(ROOT/'gramatica.txt').read_text(encoding='utf-8')
    report=(ROOT/'Informe_Laboratorio_3.md').read_text(encoding='utf-8')
    for i,(lhs,alts) in enumerate(BASE.items(),1):
        rule=f'R{i}. {lhs} → '+' | '.join(' '.join(rhs) for rhs in alts)
        check(f'R{i}: transcripción en gramatica.txt',rule in text)
        table='| R'+str(i)+' | `'+lhs+'` | `'+ ' ∣ '.join(' '.join(rhs) for rhs in alts)+'` |'
        check(f'R{i}: transcripción en informe',table in report)

    reference=(ROOT/'evidencias/programa_referencia.txt').read_text(encoding='utf-8')
    check('Programa de referencia completo con comentario',accepts(reference,'<programa>'))
    instructions=[x.strip()+' #' for x in re.sub(r'/\*.*?\*/','',reference,flags=re.S).split('Programa operativo_01_02',1)[1].rsplit('End',1)[0].split('#') if x.strip()]
    check('Cantidad de instrucciones originales: 20',len(instructions)==20)
    for i,source in enumerate(instructions,1): check(f'Referencia instrucción {i}: {source}',accepts(source))
    check('Espacios equivalentes',lex('z=x+y#')==lex('z = x + y #'))
    check('Espacios no concatenan identificadores',lex('x y')==[('ID','x'),('ID','y')])

    cases=[('x = 10 #',True),('z=x+y#',True),('salida z #',True),('x 10 #',False),('z=+xy#',False),('salida #',False),('x = 20',False),('Begin Programa prueba x = 5 # salida x # End',True)]
    for i,(source,expected) in enumerate(cases,1): check(f'P4 caso {i}: esperado {expected}',accepts(source,'<programa>' if i==8 else '<instruccion>')==expected)
    check('P4 caso 5 variante del PDF rechazada',not accepts('z = + x y #'))
    for source in ['x = 20 #','z = x * y #','salida temporal #']: check('P3: '+source,accepts(source))
    for op in '+-*/%': check('Operador '+op,accepts('z = x '+op+' 10 #'))
    for source in ['x=0#','x=1.345#','x=00.50#','variable_20=2#','Árbol=3#']: check('Léxico válido: '+source,accepts(source))
    for source in ['1x=5#','_x=5#','x=-5#','x=1.#','x=.5#','x=1,5#','x=1e3#','x=x+y+z#','Begin=5#','salida salida #','x y=5#','x=5#/*sin cierre']:
        check('Rechazo: '+source,not accepts(source))
    check('Programa vacío rechazado',not accepts('Begin Programa p End','<programa>'))
    check('Programa con una instrucción',accepts('Begin Programa p x=0# End','<programa>'))
    check('Instrucción no equivale a programa',not accepts('x=20#','<programa>'))
    check('Encabezado incompleto rechazado',not accepts('Begin Programa operativo_01_02','<programa>'))
    check('End ausente rechazado',not accepts('Begin Programa p x=0#','<programa>'))
    for source in ['entero x #','real temperatura #']: check('Extensión válida: '+source,accepts(source,extended=True))
    for source in ['entero 2x #','entero #','real temperatura','entero real #']: check('Extensión inválida: '+source,not accepts(source,extended=True))
    extended='Begin Programa prueba entero x # real temperatura # x=5# salida x# End'
    check('Programa extendido aceptado por G prima',accepts(extended,'<programa>',True))
    check('Programa extendido rechazado por G base',not accepts(extended,'<programa>'))
    check('Referencia preservada bajo extensión',accepts(reference,'<programa>',True))
    check('real puede ser ID en base',accepts('real=5#'))
    check('real es reservada en extensión',not accepts('real=5#',extended=True))
    specs=json.loads((ROOT/'validacion/derivaciones.json').read_text(encoding='utf-8'))
    for name,spec in specs.items():
        tree=derive(spec,EXT if name=='declaracion' else BASE)
        check('Derivación izquierda completa y árbol consistente: '+name,True)
        if name=='asignacion':
            evidence=ROOT/'evidencias/arbol_estructura.json'
            evidence.write_text(json.dumps(tree,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
            check('Lectura del árbol z = x + y #',spec['lexemas']==['z','=','x','+','y','#'])
    total=len(rows)
    rows.extend(['',f'RESULTADO: {total}/{total} comprobaciones satisfactorias.',
                 'Motor: reconocimiento general Earley sobre gramatica.json.',
                 'Alcance: análisis léxico/sintáctico; no ejecución ni análisis de tipos.',
                 'Derivaciones verificadas por sustitución del no terminal más a la izquierda.',
                 'El árbol se construye a partir de las mismas sustituciones y se comprueba nodo por nodo.'])
    (ROOT/'evidencias/validacion.txt').write_text('\n'.join(rows)+'\n',encoding='utf-8')
    print('\n'.join(rows[-6:]))

if __name__=='__main__': main()
