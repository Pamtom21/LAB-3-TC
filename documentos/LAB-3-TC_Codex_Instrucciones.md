# Instrucciones para Codex — Laboratorio 3: Diseño y Validación de Gramáticas

## Objetivo de este archivo

Este documento contiene las instrucciones que Codex debe seguir para desarrollar correctamente el **Laboratorio #3: Diseño y Validación de Gramáticas**, correspondiente a **Gramáticas Libres de Contexto (GLC)**.

Codex debe utilizar como **fuentes principales y obligatorias** los siguientes archivos entregados junto a este proyecto:

- `Laboratorio_3.pdf`
- `Formato_Informe_LAB_3.pdf`
- `Rubrica_Laboratorio_3.pdf`

No se debe reemplazar el contenido de estos documentos con supuestos externos.  
Si existe alguna ambigüedad, Codex debe priorizar:

1. El enunciado del laboratorio.
2. La plantilla/formato de informe.
3. La rúbrica de evaluación.
4. Solo después, conocimiento teórico general para explicar conceptos, sin contradecir los documentos.

---

# 1. Meta principal

Desarrollar una solución completa y coherente para el laboratorio, crear un repositorio en GitHub llamado **`LAB-3-TC`** y dejar dentro de ese repositorio todos los archivos necesarios para la entrega.

El trabajo debe:

- responder todas las preguntas solicitadas;
- utilizar correctamente la notación de Gramáticas Libres de Contexto;
- mantener consistencia entre:
  - terminales,
  - no terminales,
  - producciones,
  - símbolo inicial,
  - derivaciones,
  - árbol sintáctico,
  - validación de cadenas;
- respetar exactamente la estructura del formato de informe;
- entregar justificaciones claras;
- apuntar al nivel **Excelente** en cada criterio de la rúbrica;
- crear el repositorio de GitHub `LAB-3-TC`;
- dejar el informe completo dentro del repositorio;
- incluir los archivos complementarios necesarios para evidenciar el desarrollo.

La solución final debe quedar organizada y lista para revisión, tanto en formato Markdown como en el repositorio de GitHub.

---

# 2. Restricción de fuentes

Codex debe basarse en los archivos proporcionados.

## Fuente 1: `Laboratorio_3.pdf`

Este documento define:

- el objetivo;
- el lenguaje de referencia;
- las palabras reservadas;
- los operadores;
- las reglas de identificadores;
- las reglas de números;
- las cuatro preguntas principales;
- las cadenas que deben validarse;
- la extensión creativa;
- los entregables.

## Fuente 2: `Formato_Informe_LAB_3.pdf`

Este documento define la estructura exacta del informe.

No se debe cambiar la numeración de las secciones.

## Fuente 3: `Rubrica_Laboratorio_3.pdf`

Este documento define cómo se evaluará el laboratorio.

Cada respuesta debe ser desarrollada considerando explícitamente los criterios del nivel **Excelente**.

---

# 3. Lenguaje de referencia

Codex debe trabajar con el lenguaje simplificado definido en el laboratorio.

Programa de referencia:

```text
Begin
Programa operativo_01_02

x = 1.345 #
y = 20 #

z=x+y#
z2 = x + y #
h=z-x#
h2 = z - x #
k=h*y#
t=k/z#
m = k % 10 #

salida z #
salida h #
salida k #
salida t #
salida m #

temporal = 0 #
temporal = x #
x=y#
y = temporal #

salida x #
salida y #

End
```

---

# 4. Reglas explícitas del lenguaje

Codex debe respetar las siguientes reglas dadas por el laboratorio.

## 4.1 Palabras reservadas

```text
Begin
End
Programa
salida
```

## 4.2 Operadores aritméticos

```text
+
-
*
/
%
```

## 4.3 Operador de asignación

```text
=
```

## 4.4 Terminador de instrucción

```text
#
```

## 4.5 Identificadores

Los identificadores:

- pueden contener letras;
- pueden contener dígitos;
- pueden contener guion bajo `_`;
- deben comenzar con una letra.

Ejemplos válidos:

```text
x
z
z2
h2
temporal
operativo_01_02
```

No se deben modelar enumerando manualmente todos los identificadores posibles.

La gramática debe definir su estructura de forma general.

## 4.6 Números

El lenguaje admite números:

- enteros positivos;
- reales positivos;
- cero.

Ejemplos:

```text
0
10
20
1.345
```

Tampoco se deben enumerar manualmente todos los números posibles.

---

# 5. Estructura obligatoria del informe

Codex debe generar el contenido respetando exactamente esta estructura.

```text
1. Introducción

2. Desarrollo

2.1 Pregunta 1 – Componentes de la gramática

a) Símbolos terminales
b) Símbolos no terminales
c) Símbolo inicial
d) Definición formal de la gramática
e) Análisis

2.2 Pregunta 2 – Construcción de la Gramática Libre de Contexto

a) Producciones propuestas
b) Explicación de los no terminales
c) Verificación de la gramática

2.3 Pregunta 3 – Derivaciones y árbol sintáctico

a) Derivación por la izquierda para z = x + y #
b) Derivación para salida z #
c) Árbol de derivación
d) Explicación del árbol
e) Validación de cadenas

2.4 Pregunta 4 – Validación y detección de errores

Análisis general

3. Extensión de la gramática

4. Conclusiones
```

No cambiar esta numeración.

---

# 6. Pregunta 1 — Identificación formal de la gramática

Puntaje: **20 puntos**.

Codex debe desarrollar completamente esta sección.

## 6.1 Símbolos terminales

Clasificar los terminales en las categorías de la plantilla:

| Categoría | Elementos identificados |
|---|---|
| Palabras reservadas | |
| Operadores | |
| Símbolos especiales | |
| Identificadores | |
| Números | |

Se debe diferenciar entre:

- terminales literales;
- categorías léxicas como identificadores y números.

No se debe afirmar simplemente que cada identificador posible es un terminal enumerado individualmente.

---

## 6.2 Símbolos no terminales

Proponer no terminales suficientes para describir todo el lenguaje.

El enunciado sugiere como referencia:

```text
<programa>
<lista_instrucciones>
<instruccion>
<asignacion>
<expresion>
<salida>
```

Codex puede agregar otros si son necesarios, por ejemplo:

```text
<asignacion_simple>
<asignacion_operacion>
<operador>
<id>
<numero>
<entero>
<real>
<letra>
<digito>
```

pero todos deben justificarse y utilizarse realmente en las producciones.

Evitar no terminales redundantes o sin uso.

---

## 6.3 Símbolo inicial

Definir claramente el símbolo inicial.

Debe representar un programa completo.

Ejemplo conceptual:

```text
S = <programa>
```

La elección debe mantenerse en toda la solución.

---

## 6.4 Definición formal

Definir:

```text
G = (V, Σ, P, S)
```

Explicar claramente:

- `V`: conjunto de símbolos no terminales;
- `Σ`: conjunto de símbolos terminales;
- `P`: conjunto de producciones;
- `S`: símbolo inicial.

La definición formal debe corresponder exactamente con la gramática usada después.

No introducir símbolos aquí que luego no aparezcan en las producciones.

No usar producciones después con símbolos que nunca fueron declarados.

---

## 6.5 Análisis conceptual

Responder expresamente por qué:

- los identificadores no deben enumerarse uno por uno;
- los números no deben enumerarse uno por uno.

Explicar que ambos representan conjuntos potencialmente muy grandes o no acotados y que deben describirse mediante reglas estructurales.

La explicación debe ser breve, correcta y entendible.

---

# 7. Pregunta 2 — Construcción de la GLC

Puntaje: **30 puntos**.

Esta es la sección de mayor puntaje y debe desarrollarse con especial cuidado.

La gramática debe representar como mínimo:

1. estructura completa de programa;
2. asignación simple;
3. asignación mediante operación aritmética;
4. operadores `+ - * / %`;
5. instrucción de salida;
6. una o más instrucciones;
7. identificadores válidos;
8. números enteros y reales positivos.

---

# 8. Requisitos obligatorios de la gramática

La gramática debe permitir generar estructuras equivalentes a:

```text
Begin Programa operativo_01_02 ... End
```

Asignación simple:

```text
x = 20 #
temporal = x #
```

Asignación con operación:

```text
z = x + y #
m = k % 10 #
```

Salida:

```text
salida x #
```

Múltiples instrucciones:

```text
x = 20 #
y = 10 #
z = x + y #
salida z #
```

---

# 9. Producciones

Codex debe proponer un conjunto completo y coherente de producciones.

Punto de partida obligatorio entregado por el laboratorio:

```text
<programa> → Begin Programa <id> <lista_instrucciones> End
```

A partir de eso, completar todas las producciones.

La gramática debe distinguir explícitamente:

```text
<asignacion_simple>
```

de:

```text
<asignacion_operacion>
```

y de:

```text
<salida>
```

No mezclar estas tres estructuras sin explicación.

---

# 10. Recursividad para múltiples instrucciones

La gramática debe permitir una o más instrucciones.

Usar una estructura recursiva coherente.

Por ejemplo, conceptualmente:

```text
<lista_instrucciones> → <instruccion> <lista_instrucciones>
                     | <instruccion>
```

No copiar este ejemplo automáticamente si otra formulación resulta más coherente, pero la gramática final debe permitir múltiples instrucciones.

---

# 11. Expresiones aritméticas

La gramática debe representar como mínimo operaciones binarias de la forma:

```text
<operando> <operador> <operando>
```

con los operadores:

```text
+
-
*
/
%
```

Debe permitir ejemplos como:

```text
x + y
z - x
h * y
k / z
k % 10
```

Los operandos necesarios para el programa de referencia incluyen:

- identificadores;
- números.

---

# 12. Espacios en blanco

El programa de referencia contiene tanto:

```text
z=x+y#
```

como:

```text
z2 = x + y #
```

Codex debe tratar los espacios como elementos irrelevantes a nivel sintáctico, salvo que el profesor haya indicado lo contrario.

No crear gramáticas distintas solo por la presencia o ausencia de espacios.

En la explicación se puede señalar que el análisis léxico normalmente elimina o ignora espacios antes del análisis sintáctico.

---

# 13. Explicación de no terminales

Completar la tabla:

| No terminal | Función dentro de la gramática |
|---|---|

Cada no terminal utilizado debe tener una explicación.

Ejemplo del tipo de explicación esperado:

```text
<lista_instrucciones>
Permite representar una secuencia de una o más instrucciones dentro del programa.
```

Evitar definiciones vagas como:

```text
"Sirve para instrucciones."
```

---

# 14. Verificación contra el programa de referencia

Después de construir la gramática, verificar explícitamente que puede representar todas las estructuras del programa original.

Comprobar al menos:

- nombre del programa `operativo_01_02`;
- número real `1.345`;
- entero `20`;
- operaciones con `+`;
- operaciones con `-`;
- operaciones con `*`;
- operaciones con `/`;
- operaciones con `%`;
- asignaciones entre identificadores;
- salidas;
- múltiples instrucciones;
- `Begin`;
- `Programa`;
- `End`.

Si alguna producción propuesta no permite uno de estos casos, corregir la gramática antes de continuar.

---

# 15. Pregunta 3 — Derivaciones y árbol sintáctico

Puntaje: **25 puntos**.

Todas las derivaciones deben basarse exactamente en la gramática creada en la Pregunta 2.

No inventar una gramática diferente para facilitar una derivación.

---

# 16. Derivación por la izquierda de `z = x + y #`

Realizar una derivación por la izquierda completa.

En cada paso:

1. identificar el no terminal más a la izquierda;
2. aplicar una producción válida;
3. mostrar la nueva forma sentencial;
4. continuar hasta obtener únicamente terminales.

La cadena final debe ser:

```text
z = x + y #
```

o su equivalente sin espacios:

```text
z=x+y#
```

dependiendo del tratamiento léxico explicado.

Usar una notación consistente, por ejemplo:

```text
⇒
```

para indicar cada paso.

---

# 17. Derivación por la izquierda de `salida z #`

Realizar el mismo proceso para:

```text
salida z #
```

Debe quedar claro qué producción genera la instrucción de salida.

---

# 18. Árbol de derivación

Construir un árbol sintáctico para:

```text
z = x + y #
```

El árbol debe:

- comenzar en el símbolo inicial pertinente para una instrucción o derivación según la gramática usada;
- contener nodos no terminales internos;
- terminar en hojas terminales;
- corresponder exactamente con la derivación presentada.

Si se genera el árbol con Mermaid, Graphviz u otra herramienta, comprobar que sea legible.

No dibujar un árbol que utilice producciones inexistentes.

---

# 19. Explicación del árbol

Explicar claramente:

- qué representa la raíz;
- qué representan los nodos no terminales;
- qué representan los terminales;
- qué representan las hojas;
- cómo la lectura de las hojas produce la cadena final.

Debe ser una explicación conceptual, no solo una descripción visual.

---

# 20. Validación de cadenas de la Pregunta 3

Determinar si la gramática puede generar:

```text
x = 20 #
z = x * y #
salida temporal #
```

Para cada una indicar:

```text
Sí / No
```

y justificar usando las producciones concretas de la gramática.

No responder únicamente “sí” o “no”.

---

# 21. Pregunta 4 — Validación y detección de errores

Puntaje: **25 puntos**.

Analizar exactamente estos ocho casos:

| Caso | Cadena |
|---|---|
| 1 | `x = 10 #` |
| 2 | `z=x+y#` |
| 3 | `salida z #` |
| 4 | `x 10 #` |
| 5 | `z=+xy#` |
| 6 | `salida #` |
| 7 | `x = 20` |
| 8 | `Begin Programa prueba x = 5 # salida x # End` |

Para el caso 8, considerar la estructura completa del programa, aunque en el PDF aparezca visualmente separada por `/`.

---

# 22. Cómo validar cada caso

Para cada cadena:

1. indicar si pertenece al lenguaje;
2. identificar qué producción o estructura permite generarla;
3. si es inválida, señalar exactamente:
   - qué símbolo falta;
   - qué símbolo está mal posicionado;
   - qué estructura de la gramática se incumple.

Ejemplo del nivel de precisión esperado:

```text
No pertenece al lenguaje porque una asignación requiere el operador "=" entre el identificador y el valor.
```

Evitar explicaciones demasiado generales como:

```text
"Está mal escrita."
```

---

# 23. Análisis general de errores

Después de la tabla de casos, escribir un análisis breve indicando los errores sintácticos principales detectados.

Entre los tipos de errores que deben revisarse están:

- ausencia del operador `=`;
- posición incorrecta del operador aritmético;
- ausencia del identificador en una salida;
- ausencia del terminador `#`;
- estructura incompleta de una producción.

La explicación debe relacionarse con la gramática desarrollada.

---

# 24. Extensión creativa de la gramática

El laboratorio exige agregar una nueva construcción sintáctica.

Opciones disponibles:

```text
A. Condicional
B. Repetición
C. Declaración de variables
D. Salida de texto
E. Propuesta propia
```

Codex debe escoger **una sola** y desarrollarla completamente.

---

# 25. Recomendación para la extensión

Elegir una alternativa que sea:

- simple de explicar;
- fácil de integrar a la gramática;
- fácil de derivar;
- fácil de validar.

Preferentemente seleccionar:

```text
C. Declaración de variables
```

o:

```text
D. Salida de texto
```

porque requieren menos cambios estructurales que un condicional o ciclo.

Si se selecciona otra alternativa, mantenerla coherente.

---

# 26. Requisitos de la extensión

La extensión debe incluir obligatoriamente:

1. construcción seleccionada;
2. nueva sintaxis propuesta;
3. nuevos terminales;
4. nuevos no terminales;
5. nuevas producciones;
6. ejemplo de cadena válida;
7. ejemplo de cadena inválida;
8. derivación de ejemplo.

Además, debe incorporarse formalmente a la gramática.

No basta con describirla en texto.

---

# 27. Conclusiones

Escribir entre uno y dos párrafos.

La conclusión debe mencionar aprendizajes reales del laboratorio, por ejemplo:

- diferencia entre terminales y no terminales;
- función de las producciones;
- importancia del símbolo inicial;
- utilidad de las derivaciones;
- relación entre gramática y árbol sintáctico;
- validación de cadenas;
- importancia de mantener coherencia interna.

Evitar una conclusión genérica o desconectada del trabajo realizado.

---

# 28. Criterios de la rúbrica que se deben cumplir

Codex debe revisar la solución final usando los siguientes objetivos.

## P1 — Identificación formal — 20 puntos

Para nivel Excelente:

- terminales correctamente identificados;
- no terminales correctamente identificados;
- símbolo inicial correcto;
- definición precisa de `G = (V, Σ, P, S)`;
- explicación conceptual clara.

---

## P2 — Construcción de la GLC — 30 puntos

Para nivel Excelente:

- gramática correcta;
- gramática coherente;
- representa todas las estructuras solicitadas;
- permite múltiples instrucciones;
- producciones claras;
- producciones justificadas.

---

## P3 — Derivaciones y árbol — 25 puntos

Para nivel Excelente:

- derivaciones por la izquierda completas;
- derivaciones correctas;
- árbol sintáctico consistente;
- explicación clara de la relación entre nodos y símbolos.

---

## P4 — Validación y errores — 25 puntos

Para nivel Excelente:

- clasificar correctamente todas las cadenas;
- justificar cada caso;
- detectar exactamente los elementos sintácticos faltantes;
- detectar símbolos incorrectos o mal ubicados.

---

# 29. Criterios transversales

Codex debe realizar una revisión global antes de finalizar.

## 29.1 Coherencia interna

La misma gramática debe utilizarse en:

- producciones;
- derivaciones;
- árboles;
- validaciones.

No modificar las reglas entre una sección y otra.

---

## 29.2 Notación

Usar notación consistente.

Ejemplo:

```text
<programa>
<instruccion>
<id>
```

No alternar innecesariamente entre:

```text
<id>
ID
identificador
```

si todos representan exactamente el mismo no terminal.

---

## 29.3 Justificación

Toda respuesta importante debe incluir explicación.

Una respuesta correcta sin justificación puede perder puntaje.

---

## 29.4 Presentación

Todo debe quedar:

- legible;
- ordenado;
- con tablas completas;
- con producciones alineadas;
- con derivaciones fáciles de seguir;
- con árbol sintáctico comprensible.

---

# 30. Comprobación automática de coherencia

Antes de entregar la solución, Codex debe ejecutar mentalmente o mediante código las siguientes comprobaciones.

## Check 1

¿Todos los no terminales usados en las producciones están declarados en `V`?

## Check 2

¿Todos los terminales usados en las producciones están incluidos en `Σ` o explicados como categorías léxicas?

## Check 3

¿Existe un único símbolo inicial claramente definido?

## Check 4

¿La gramática puede generar más de una instrucción?

## Check 5

¿Puede generar:

```text
x = 1.345 #
```

?

## Check 6

¿Puede generar:

```text
m = k % 10 #
```

?

## Check 7

¿Puede generar:

```text
temporal = x #
```

?

## Check 8

¿Puede generar:

```text
salida temporal #
```

?

## Check 9

¿Puede generar el encabezado:

```text
Begin Programa operativo_01_02
```

?

## Check 10

¿Puede terminar correctamente con:

```text
End
```

?

## Check 11

¿Las derivaciones usan únicamente producciones existentes?

## Check 12

¿El árbol usa exactamente las mismas reglas que la derivación?

## Check 13

¿Las validaciones de la Pregunta 4 son compatibles con la gramática?

## Check 14

¿La extensión creativa fue agregada formalmente?

---


# 31. Creación obligatoria del repositorio de GitHub

Codex debe crear un repositorio de GitHub llamado exactamente:

```text
LAB-3-TC
```

El repositorio debe contener el desarrollo completo del laboratorio.

## 31.1 Requisitos del repositorio

El repositorio debe incluir como mínimo:

```text
LAB-3-TC/
├── README.md
├── Informe_Laboratorio_3.md
├── gramatica.txt
├── arbol_derivacion.mmd
├── evidencias/
└── documentos/
```

La estructura puede ampliarse si es necesario, pero no deben faltar el informe y el README.

## 31.2 README obligatorio

Crear un `README.md` que incluya:

- nombre del laboratorio;
- asignatura;
- tema;
- objetivo general;
- breve descripción del contenido del repositorio;
- estructura de carpetas;
- explicación de cómo visualizar el árbol sintáctico;
- enlace o referencia al informe principal;
- integrantes, si esa información está disponible;
- indicación de que el trabajo corresponde al Laboratorio 3 de Teoría de la Computación.

Ejemplo de título:

```markdown
# LAB-3-TC

Laboratorio 3 — Diseño y Validación de Gramáticas Libres de Contexto
```

## 31.3 Archivos fuente del laboratorio

Crear la carpeta:

```text
documentos/
```

y copiar o dejar referenciados dentro de ella los documentos fuente utilizados para el desarrollo, siempre que estén disponibles localmente:

```text
Laboratorio_3.pdf
Formato_Informe_LAB_3.pdf
Rubrica_Laboratorio_3.pdf
```

Si Codex no puede copiar directamente alguno de estos archivos, no debe inventarlo. Debe continuar con el resto del trabajo y dejar indicado en el README qué documentos se utilizaron como fuente.

## 31.4 Evidencias

Crear una carpeta:

```text
evidencias/
```

para guardar elementos como:

- imagen o exportación del árbol sintáctico;
- capturas de validación;
- archivo de JFLAP, si se utiliza;
- otros recursos generados durante el desarrollo.

Si se usa Mermaid:

```text
arbol_derivacion.mmd
```

Si se usa Graphviz:

```text
arbol_derivacion.dot
```

Puede además exportarse una versión visual:

```text
evidencias/arbol_derivacion.png
```

o equivalente.

## 31.5 Inicialización del repositorio

Codex debe ejecutar los pasos necesarios para crear el repositorio local.

Ejemplo:

```bash
mkdir LAB-3-TC
cd LAB-3-TC

git init
```

Luego debe crear los archivos del proyecto.

Después:

```bash
git add .
git commit -m "Laboratorio 3 Teoria de la Computacion"
```

## 31.6 Creación del repositorio remoto

Si GitHub CLI (`gh`) está instalado y autenticado, usar preferentemente:

```bash
gh repo create LAB-3-TC --public --source=. --remote=origin --push
```

Si por alguna razón se desea un repositorio privado, solo hacerlo si el usuario lo solicita explícitamente.

Por defecto, crear el repositorio como:

```text
public
```

## 31.7 Si el repositorio ya existe

Antes de crear el repositorio remoto, verificar si `LAB-3-TC` ya existe en la cuenta de GitHub autenticada.

Si existe:

- no sobrescribirlo destructivamente;
- revisar su contenido;
- reutilizarlo si corresponde al mismo laboratorio;
- agregar o actualizar los archivos necesarios;
- evitar eliminar archivos que no hayan sido creados por esta tarea.

## 31.8 Verificación de Git

Antes de finalizar comprobar:

```bash
git status
```

El estado final ideal debe indicar que no existen cambios pendientes.

También comprobar:

```bash
git log --oneline -5
```

y confirmar que exista al menos un commit con el desarrollo del laboratorio.

## 31.9 Verificación del remoto

Comprobar:

```bash
git remote -v
```

Debe existir un remoto:

```text
origin
```

apuntando al repositorio `LAB-3-TC`.

## 31.10 Resultado esperado en GitHub

El repositorio debe mostrar, como mínimo:

```text
README.md
Informe_Laboratorio_3.md
gramatica.txt
arbol_derivacion.mmd
evidencias/
documentos/
```

El `README.md` debe permitir comprender rápidamente qué contiene el repositorio y dónde se encuentra el informe.

---

# 32. Formato de salida solicitado a Codex


Codex debe generar dentro del repositorio `LAB-3-TC`, como mínimo:

```text
README.md
Informe_Laboratorio_3.md
gramatica.txt
arbol_derivacion.mmd
```

El archivo:

```text
Informe_Laboratorio_3.md
```

debe contener todo el desarrollo académico.

El archivo:

```text
gramatica.txt
```

debe contener la gramática final limpia y consistente.

El archivo:

```text
arbol_derivacion.mmd
```

debe contener el árbol de derivación si se utiliza Mermaid.

Si se utiliza Graphviz, crear en su lugar o adicionalmente:

```text
arbol_derivacion.dot
```

También se deben usar las carpetas:

```text
evidencias/
documentos/
```

según lo indicado en la sección de GitHub.

---

# 33. Estructura recomendada para `Informe_Laboratorio_3.md`

```markdown
# INFORME DE LABORATORIO #3

## Gramáticas Libres de Contexto

### Antecedentes

- Asignatura:
- Carrera:
- Docente:
- Integrantes:
- Fecha:

# 1. Introducción

...

# 2. Desarrollo

## 2.1 Pregunta 1 – Componentes de la gramática

### a) Símbolos terminales

...

### b) Símbolos no terminales

...

### c) Símbolo inicial

...

### d) Definición formal de la gramática

...

### e) Análisis

...

## 2.2 Pregunta 2 – Construcción de la Gramática Libre de Contexto

### a) Producciones propuestas

...

### b) Explicación de los no terminales

...

### c) Verificación de la gramática

...

## 2.3 Pregunta 3 – Derivaciones y árbol sintáctico

### a) Derivación por la izquierda para z = x + y #

...

### b) Derivación para salida z #

...

### c) Árbol de derivación

...

### d) Explicación del árbol

...

### e) Validación de cadenas

...

## 2.4 Pregunta 4 – Validación y detección de errores

...

### Análisis general

...

# 3. Extensión de la gramática

...

# 4. Conclusiones

...
```

---

# 34. Reglas de calidad de redacción

El informe debe usar lenguaje académico, pero claro.

Evitar:

```text
"Esto funciona porque sí."
```

Preferir:

```text
"La producción permite generar una asignación simple porque establece un identificador en el lado izquierdo, seguido del operador de asignación, un valor válido y el terminador de instrucción."
```

No extender innecesariamente las explicaciones.

Cada explicación debe demostrar comprensión del concepto evaluado.

---

# 35. No hacer

Codex NO debe:

- omitir preguntas;
- cambiar la estructura de la plantilla;
- inventar ejemplos que contradigan la gramática;
- utilizar una gramática para las derivaciones y otra para las validaciones;
- enumerar todos los identificadores posibles;
- enumerar todos los números posibles;
- entregar derivaciones sin pasos;
- entregar un árbol que no corresponda a las producciones;
- responder validaciones solo con “sí” o “no”;
- agregar una extensión sin modificar formalmente la gramática;
- usar símbolos no declarados;
- declarar producciones que nunca se usan;
- eliminar `#` como terminador;
- olvidar alguno de los operadores `+ - * / %`;
- olvidar que los identificadores deben comenzar con una letra.

---

# 36. Instrucción final para Codex

Ejecuta el trabajo de principio a fin.

1. Lee completamente:
   - `Laboratorio_3.pdf`;
   - `Formato_Informe_LAB_3.pdf`;
   - `Rubrica_Laboratorio_3.pdf`.

2. Extrae todos los requerimientos.

3. Diseña primero una única gramática coherente.

4. Verifica que represente todo el programa de referencia.

5. Usa esa misma gramática para:
   - la definición formal;
   - las derivaciones;
   - el árbol;
   - la validación de cadenas.

6. Desarrolla las cuatro preguntas.

7. Agrega una extensión creativa completa.

8. Redacta introducción y conclusiones.

9. Revisa la solución usando la rúbrica.

10. Corrige cualquier inconsistencia antes de generar el archivo final.

11. Crea el repositorio local:

```text
LAB-3-TC
```

12. Dentro del repositorio crea:

```text
README.md
Informe_Laboratorio_3.md
gramatica.txt
arbol_derivacion.mmd
evidencias/
documentos/
```

13. Inicializa Git, realiza al menos un commit y crea el repositorio remoto en GitHub.

14. Si `gh` está disponible y autenticado, utiliza:

```bash
gh repo create LAB-3-TC --public --source=. --remote=origin --push
```

15. Verifica:

```bash
git status
git log --oneline -5
git remote -v
```

16. Confirma que el repositorio remoto contiene el informe completo y los archivos complementarios.

17. Entrega como resultado final:

```text
Repositorio GitHub: LAB-3-TC
Informe principal: Informe_Laboratorio_3.md
```

El informe debe quedar completo, ordenado y listo para revisión o conversión posterior a PDF.

---

# 37. Criterio final de aceptación

El trabajo se considera terminado únicamente si:

- todas las secciones del formato están completas;
- la gramática representa el programa de referencia;
- todas las derivaciones son correctas;
- el árbol coincide con la gramática;
- todas las cadenas fueron validadas;
- los errores están justificados;
- la extensión creativa está incorporada;
- la notación es consistente;
- no existen contradicciones entre secciones;
- existe un repositorio GitHub llamado exactamente `LAB-3-TC`;
- el repositorio contiene `README.md` e `Informe_Laboratorio_3.md`;
- existe al menos un commit;
- el remoto `origin` está configurado correctamente;
- los archivos principales están subidos al repositorio;
- el resultado apunta al nivel **Excelente** de la rúbrica.
