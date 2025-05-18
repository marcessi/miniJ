# miniJ: Intérprete para un subconjunto de J

## Descripción

miniJ es un intérprete para un subconjunto del lenguaje de programación J, implementado como parte de un proyecto académico. El intérprete procesa código en la sintaxis de J utilizando una gramática ANTLR y lo ejecuta utilizando numpy para las operaciones de arrays.

## Características

El intérprete soporta las siguientes características del lenguaje J:

- **Arrays y operaciones básicas**: Manipulación de arrays numéricos con operaciones como suma, resta, multiplicación, división entera, módulo y potencia.
- **Variables y asignación**: Almacenamiento de valores en variables con el operador `=:`.
- **Operadores aritméticos**: `+`, `-`, `*`, `%` (división), `|` (módulo), `^` (potencia).
- **Operadores relacionales**: `>`, `<`, `>=`, `<=`, `=`, `<>`.
- **Operadores especiales**: 
  - `]` (identidad)
  - `,` (concatenación)
  - `#` (tamaño y filtrado)
  - `{` (indexación)
  - `i.` (generación de secuencias)
- **Modificadores**:
  - `:` (aplicación de operador a un valor consigo mismo)
  - `/` (fold/reducción)
  - `~` (flip/inversión de argumentos)
- **Definición de funciones**: Mediante asignación y composición.
- **Composición de funciones**: Con el operador `@:`.

## Sintaxis y Operadores

### Sintaxis Básica

- **Arrays**: Se escriben como números separados por espacios: `1 2 3`
- **Comentarios**: Comienzan con `NB.` y continúan hasta el final de la línea
- **Asignación**: Se realiza con el operador `=:`: `x =: 1 2 3`
- **Valores negativos**: Se representan con un guion bajo antes del número: `_1 _2 _3`

### Operadores Aritméticos

- **Suma (`+`)**: `1 + 2` = `3`, `1 2 3 + 4 5 6` = `5 7 9`
- **Resta (`-`)**: `5 - 2` = `3`, `5 5 5 - 1 2 3` = `4 3 2`
- **Multiplicación (`*`)**: `2 * 3` = `6`, `2 * 1 2 3` = `2 4 6`
- **División (`%`)**: `6 % 2` = `3` (división entera), `10 % 3` = `3`
- **Módulo (`|`)**: `2 | 7` = `1`, `3 | 10` = `1` (nota: los operandos están al revés que en otros lenguajes)
- **Potencia (`^`)**: `2 ^ 3` = `8`, `2 ^ 1 2 3` = `2 4 8`

### Operadores Relacionales

- **Mayor (`>`)**: `2 > 1` = `1`, `2 > 2` = `0`
- **Menor (`<`)**: `1 < 2` = `1`, `2 < 2` = `0`
- **Mayor o igual (`>=`)**: `2 >= 2` = `1`, `1 >= 2` = `0`
- **Menor o igual (`<=`)**: `2 <= 2` = `1`, `3 <= 2` = `0`
- **Igual (`=`)**: `2 = 2` = `1`, `2 = 3` = `0`
- **Distinto (`<>`)**: `2 <> 3` = `1`, `2 <> 2` = `0`

### Operadores Especiales

- **Identidad (`]`)**: `] 1 2 3` = `1 2 3`
- **Tamaño (`#`)**: `# 1 2 3` = `3`
- **Filtrado (`#`)**: `1 0 1 # 1 2 3` = `1 3` (filtra usando una máscara de unos y ceros)
- **Concatenación (`,`)**: `1 , 2 3` = `1 2 3`
- **Indexación (`{`)**: `1 { 10 20 30` = `20` (indexación basada en cero)
- **Secuencia (`i.`)**: `i. 5` = `0 1 2 3 4` (genera los primeros n números naturales)

### Modificadores

- **Duplicación (`:`)**: Convierte un operador binario en unario que aplica la operación al valor consigo mismo:
  - `+: 3` = `6` (equivale a `3 + 3`)
  - `*: 4` = `16` (equivale a `4 * 4`)
  - `-: 5` = `0` (equivale a `5 - 5`)
  - `<=: 3` = `1` (equivale a `3 <= 3`)

- **Reducción (`/`)**: Aplica la operación de forma acumulativa a todos los elementos:
  - `+/ 1 2 3 4` = `10` (suma: 1+2+3+4)
  - `*/ 1 2 3 4` = `24` (producto: 1*2*3*4)
  - `=/ 3 3 3 3` = `1` (comprueba si todos son iguales)
  - `</ 1 2 3 4` = `1` (comprueba si está ordenado estrictamente)
  - `<=/ 1 2 2 3` = `1` (comprueba si está ordenado)

- **Inversión de argumentos (`~`)**: Invierte el orden de los argumentos en operadores binarios:
  - `2 +~ 3` = `5` (equivale a `3 + 2`)
  - `2 |~ 7` = `1` (equivale a `7 | 2`)

### Definición de Funciones en miniJ

miniJ permite definir funciones de diversas formas, ofreciendo flexibilidad similar a J:

#### Tipos de Definiciones

1. **Función literal con operador binario y argumento derecho**
   - `double =: 2 * ]` (multiplica el argumento por 2)
   - `add5 =: 5 + ]` (suma 5 al argumento)

2. **Función literal con operador binario y argumento izquierdo**
   - `reciprocal =: ] % 2` (divide el argumento entre 2)
   - `subtract_from_10 =: 10 - ]` (resta el argumento de 10)

3. **Función con operador binario entre dos funciones**
   - `mean_square =: (+/ % #) @: *:` (media de los cuadrados)
   - `is_above_avg =: ] > +/ % #` (comprueba si cada elemento supera la media)
   - `pos_diff =: +/ @: (] > 0) - (] < 0)` (diferencia entre el numero de positivos y negativos)

4. **Funciones unarias (operadores especiales y modificadores)**
   - `identity =: ]` (devuelve el argumento sin cambios)
   - `size =: #` (devuelve la longitud del array)
   - `sequence =: i.` (genera secuencia desde 0 hasta n-1)
   - `square =: *:` (eleva el argumento al cuadrado)
   - `all_different =: <>/` (comprueba si todos los elementos son diferentes)


#### Composición de Funciones

La composición de funciones en miniJ se realiza con el operador `@:`, permitiendo encadenar operaciones:

1. **Composición básica**:
   - `square_then_double =: +: @: *:` (primero cuadrado, luego duplica)

2. **Composición múltiple**:
   - `add1 =: 1 + ]`
   - `double =: +:` 
   - `square =: *:`
   - `complex_fn =: square @: double @: add1` (suma 1, duplica, y luego eleva al cuadrado)

#### Aplicación de Funciones

En miniJ, las funciones se aplican simplemente escribiendo la función seguida del argumento:

- **Ejemplos básicos**:
  - `double 3` = `6` (aplicar a un escalar)
  - `square 1 2 3` = `1 4 9` (aplicar a un array)
  - `sum_of_squares 1 2 3` = `14` (función compuesta)

#### Asociatividad en Funciones

En miniJ, las operaciones tienen asociatividad por la derecha, lo que afecta la forma en que se evalúan las expresiones:

1. **Asociatividad en composiciones**:
   - `f @: g @: h` se evalúa como `f @: (g @: h)`, aplicando primero `h`, luego `g` y finalmente `f`.

2. **Asociatividad en operaciones**:
   - `2 * 3 + 4` se evalúa como `2 * (3 + 4)` = `2 * 7` = `14`
   - `5 - 2 - 1` se evalúa como `5 - (2 - 1)` = `5 - 1` = `4`

## Detalles de Implementación

- **Gramática ANTLR**: Define la sintaxis del lenguaje con reglas para expresiones, operadores, y precedencia.
- **Visitor Pattern**: Implementado en Python para interpretar y ejecutar el código.
- **Numpy**: Utilizado para operaciones vectoriales eficientes.

## Cómo Ejecutar

### Requisitos
- Python 3
- ANTLR4 Runtime
- Numpy

### Instrucciones de instalación

1. Instala las herramientas de ANTLR4 y su runtime para Python:
   ```
   pip install antlr4-tools
   antlr4
   pip install antlr4-python3-runtime
   pip install numpy
   ```

   **Nota para usuarios de Windows**: Puede ser necesario realizar pasos adicionales para configurar ANTLR4 correctamente. Consulta la [referencia de antlr4-tools](https://github.com/antlr/antlr4-tools) para más detalles.

2. Compila el proyecto usando make:
   ```
   make
   ```

3. Ejecuta el intérprete en un archivo de prueba:
   ```
   python3 g.py tests/basic.j
   ```

## Limitaciones

- Solo trabaja con números enteros
- No implementa todas las características avanzadas de J
- No soporta arrays multidimensionales
- Las funciones solo pueden operar sobre un parámetro
- Algunos operadores tienen comportamiento simplificado
