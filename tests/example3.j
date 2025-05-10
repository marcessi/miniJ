NB. Funciones básicas
square =: *:
square 1 2 3 4        NB. resultado: 1 4 9 16
square 1 + i. 3       NB. resultado: 1 4 9

NB. Función identidad
id =: ]
id 5 6 7             NB. resultado: 5 6 7

NB. Funciones con operador binario e identidad
mod2 =: 2 | ]
mod2 i. 6            NB. resultado: 0 1 0 1 0 1
mod3 =: 3 | ]
mod3 i. 8            NB. resultado: 0 1 2 0 1 2 0 1

NB. Composición de funciones
eq0 =: 0 = ]
parell =: eq0 @: mod2
parell i. 6          NB. resultado: 1 0 1 0 1 0

NB. Uso directo de funciones sin composición explícita
eq0 mod2 i. 6        NB. resultado: 1 0 1 0 1 0

NB. Composición directa sin variables intermedias
parell =: 0 = ] @: 2 | ]
parell i. 6          NB. resultado: 1 0 1 0 1 0

NB. Múltiples niveles de composición
inc =: 1 + ]
test =: +/ @: inc @: i.
test 3               NB. resultado: 6

NB. Funciones con modificadores y operaciones
double =: +:
double 3 4 5         NB. resultado: 6 8 10

NB. Funciones de reducción (fold)
sum =: +/
sum 1 2 3 4 5        NB. resultado: 15
product =: */
product 1 2 3 4      NB. resultado: 24

NB. Funciones de operación con valores específicos
add5 =: 5 + ]
add5 i. 5            NB. resultado: 5 6 7 8 9

NB. Combinación de operaciones con composición
sumSquares =: +/ @: *:
sumSquares 1 2 3     NB. resultado: 14
doubleSum =: +: @: +/
doubleSum 1 2 3      NB. resultado: 12

NB. Funciones que retornan el resultado de otra función aplicada
squareSum =: square @: sum
squareSum 1 2 3      NB. resultado: 36

NB. Funciones con operaciones inversas
triple =: 3 * ]
doubleTriple =: double @: triple
doubleTriple 2       NB. resultado: 12

NB. Operaciones de comparación como funciones
greaterThan3 =: 3 < ]
greaterThan3 2 3 4 5  NB. resultado: 0 0 1 1
isPositive =: 0 < ]
isPositive _2 0 3    NB. resultado: 0 0 1

NB. Funciones que generan secuencias
sequence =: i.
sequence 4           NB. resultado: 0 1 2 3

NB. Generadores de secuencias con operaciones
NB. oneToN =: >: @: i.
NB. oneToN 5             NB. resultado: 1 2 3 4 5

NB. Funciones más complejas
NB. factorial =: */ @: >: @: i.
NB. factorial 5          NB. resultado: 120