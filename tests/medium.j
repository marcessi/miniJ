NB. Test file for miniJ interpreter
NB. Advanced tests focusing on function composition and advanced operators

NB. ======= ADVANCED FUNCTION COMPOSITION =======
NB. Función que comprueba si un número es mayor que 5
gt5 =: 5 < ]
gt5 7 3 6 4            NB. resultado: 1 0 1 0

NB. Función que comprueba si un número es primo (simplificado para números pequeños)
mod2 =: 2 | ]
mod3 =: 3 | ]
not_div_by_2 =: 0 <> ] @: mod2
not_div_by_3 =: 0 <> ] @: mod3
mask1 =: not_div_by_2 2 3 4 5 6 7 8 9 10
mask2 =: not_div_by_3 2 3 4 5 6 7 8 9 10
mask_primes =: (mask1 * mask2) + 1 1 0 0 0 0 0 0 0
primes =: mask_primes # ]
primes 2 3 4 5 6 7 8 9 10  NB. resultado: 2 3 5 7

NB. Función compuesta con múltiples operaciones
square =: *:
double =: 2 * ]
add1 =: 1 + ]
complex_fn =: square @: double @: add1
complex_fn 1 2 3        NB. resultado: 16 36 64  NB. ((1+1)*2)², ((2+1)*2)², ((3+1)*2)²

NB. ======= FOLD CON OPERADORES RELACIONALES =======
NB. Comprueba si todos los elementos son positivos
all_positive =: */ @: 0 < ]
all_positive 1 2 3 4     NB. resultado: 1  NB. Todos son > 0
all_positive _1 2 3 4    NB. resultado: 0  NB. No todos son > 0

NB. Comprueba si algún elemento es mayor que 5
any_gt5 =: +/ @: 5 < ]
any_gt5 1 2 3 4         NB. resultado: 0  NB. Ningún elemento > 5
any_gt5 1 6 3 7         NB. resultado: 2  NB. Dos elementos > 5

NB. Comprueba si todos los elementos son iguales
all_equal =: =/
all_equal 3 3 3 3       NB. resultado: 1  NB. Todos iguales
all_equal 3 3 2 3       NB. resultado: 0  NB. No todos iguales

NB. Comprueba si es una secuencia ordenada crecientemente
ordered =: <=/
ordered 1 2 3 4 5       NB. resultado: 1  NB. Creciente
ordered 1 2 4 3 5       NB. resultado: 0  NB. No creciente

NB. ======= OPERADORES CON : =======
NB. Operador : aplica la operación con el elemento y sí mismo
+: 3 4 5               NB. resultado: 6 8 10  NB. Equivalente a 3+3, 4+4, 5+5
-: 3 4 5               NB. resultado: 0 0 0  NB. Equivalente a 3-3, 4-4, 5-5
*: 2 3 4               NB. resultado: 4 9 16  NB. Equivalente a 2*2, 3*3, 4*4
%: 6 10 15             NB. resultado: 1 1 1   NB. División por sí mismo (x%x=1)
|: 5 6 7               NB. resultado: 0 0 0   NB. Módulo consigo mismo (siempre 0)
^: 2 3 4               NB. resultado: 4 27 256 NB. Equivalente a 2^2, 3^3, 4^4

NB. Operadores relacionales con :
>: 3 4 5               NB. resultado: 0 0 0  NB. Eq. a 3>3, 4>4, 5>5 (siempre falso)
<: 3 4 5               NB. resultado: 0 0 0  NB. Eq. a 3<3, 4<4, 5<5 (siempre falso)
<=: 3 4 5              NB. resultado: 1 1 1  NB. Eq. a 3<=3, 4<=4, 5<=5 (siempre verdadero)
<>: 3 4 5              NB. resultado: 0 0 0  NB. Eq. a 3<>3, 4<>4, 5<>5 (siempre falso)

NB. Uso práctico de operadores con :
square =: *:           NB. Define la función square usando *:
square 1 2 3           NB. resultado: 1 4 9
double =: +:           NB. Define la función double usando +:
double 1 2 3           NB. resultado: 2 4 6

NB. Combinaciones de operadores con : y otros operadores
double_square =: +: @: *:
double_square 2 3 4    NB. resultado: 8 18 32  NB. (2*2)*2, (3*3)*2, (4*4)*2

NB. En lugar de sign_test que resta dos funciones, usamos:
pos =: 0 < ]
neg =: 0 > ]
zero =: 0 = ]
pos 3              NB. resultado: 1
pos _3             NB. resultado: -1
neg _2             NB. resultado: 1
neg 2              NB. resultado: 1
zero 0             NB. resultado: 1
zero 1             NB. resultado: 1

NB. Calcular la media de un vector
sum =: +/ @: ]
count =: # @: ]
mean =: +/ 2 4 6 8 % count 2 4 6 8
mean           NB. resultado: 5  NB. (2+4+6+8)/4 = 20/4 = 5

NB. ======= CASOS DE USO PRÁCTICOS =======
NB. Filtrar números pares de una secuencia
nums =: i. 10
evens_mask_func =: 0 = ] @: mod2
evens_mask =: evens_mask_func nums
evens =: evens_mask # nums
evens                    NB. resultado: 0 2 4 6 8

NB. Calcular el producto de los números impares de una secuencia
odds_mask_func =: 1 = ] @: mod2
odds_mask =: odds_mask_func nums
odds =: odds_mask # nums
odds                    NB. resultado: 1 3 5 7 9
prod_odds =: */
prod_odds odds          NB. resultado: 945  NB. 1*3*5*7*9 = 945

NB. Función que calcula la suma de los cuadrados de los números pares
sqsum_evens =: +/ @: square @: ]
sqsum_evens evens       NB. resultado: 120  NB. 0²+2²+4²+6²+8² = 0+4+16+36+64 = 120

NB. Aplicar múltiples operaciones y luego comparar resultados
op1 =: +/ @: square
op2 =: */ @: add1
compare0 =: op1 1 2 3
compare1 =: op2 1 2 3
compare0 > compare1     NB. resultado: 0  NB. 1²+2²+3² < (1+1)*(2+1)*(3+1) → 14 < 24
compare0                NB. resultado: 14
compare1                NB. resultado: 24

NB. Función que devuelve índices de elementos que cumplen una condición
indices =: i. @: #
gt5_mask =: 5 < ]

NB. Aplicamos cada función por separado
test_array =: 3 8 2 9 4
idx =: indices test_array    NB. resultado: 0 1 2 3 4
idx
mask =: gt5_mask test_array  NB. resultado: 0 1 0 1 0
mask
result =: mask # idx         NB. resultado: 1 3  NB. Índices donde elementos > 5
result