NB. ======= COMPOSICIONES ANIDADAS Y TRANSFORMACIONES EN CADENA =======

NB. Promedio de los cuadrados de los elementos pares de una secuencia
nums =: i. 10
is_even =: 0 = ] @: (2 | ])
evens =: (is_even nums) # nums
squares =: *: evens
mean =: +/ squares % # squares
mean                   NB. resultado: 24  NB. (0²+2²+4²+6²+8²)/5 = 120/5 = 24

NB. Contar cuántos elementos de una lista son mayores que el promedio
data =: 3 6 9 12 15
avg =: +/ data % # data
gt_avg =: avg < ]
mask =: gt_avg data
mask                     NB. resultado: 0 0 0 1 1
+/ mask                  NB. resultado: 2  NB. Dos mayores que la media

NB. Función que da 1 solo si todos los elementos son pares y están ordenados
is_even =: 0 = ] @: 2 | ]
ordered =: <=/
all_even_ordered =: */ @: (is_even * ordered)
all_even_ordered 2 4 6 8   NB. resultado: 1
all_even_ordered 2 5 6 8   NB. resultado: 0

NB. ======= FUNCIONES DE MÁSCARA COMPLEJAS =======

NB. Dado un vector, seleccionar los elementos impares mayores que 3
is_odd =: 1 = ] @: 2 | ]
gt3 =: 3 < ]
odd_gt3 =: is_odd * gt3
vec =: 1 2 3 4 5 6 7
odd_gt3_mask =: odd_gt3 vec
filtered =: odd_gt3_mask # vec
filtered                NB. resultado: 5 7

NB. Función: suma acumulada de los cuadrados de los elementos impares de una secuencia
odds =: (is_odd nums) # nums
sum_sq_odds =: +/ @: *: @: ]
odds
sum_sq_odds odds        NB. resultado: 165  NB. 1²+3²+5²+7²+9² = 165

NB. ======= COMPOSICIÓN EN CASCADA DE MÁS DE 3 FUNCIONES =======

NB. ((x * 2) + 1)^2 - 3
final_fn =: ] - 3 @: *: @: 1 + ] @: 2 * ]
final_fn 1 2 3          NB. resultado: 6 22 46  NB. (((x*2)+1)^2) - 3

NB. Vector de longitud 10, invertirlo si la suma es > 25
vec =: 0 1 2 3 4 5 6 7 8 9
sum =: +/ vec
inv =: 9 8 7 6 5 4 3 2 1 0
cond =: 25 < sum
res =: cond * inv + (1 - cond) * vec
sum                     NB. resultado: 45
res                     NB. resultado: 9 8 7 6 5 4 3 2 1 0

NB. Mezcla de operadores especiales y aritméticos
mask =: 1 0 1 0
vals =: 10 20 30 40
5 + +/ (mask # vals)   NB. resultado: 45   NB. +/((1 0 1 0)#(10 20 30 40))+5 = (10+30)+5 = 45

NB. Mezcla de operaciones con arrays y escalares usando máscaras
mask =: 1 0 1 1 0
mask2 =: 1 1 1 1
vals =: 10 20 30 40 50
10 + (mask2 # 4 , mask # vals)   NB. resultado: 14 20 40 50   NB. 4 10 30 40 + 10 = 14 20 40 50

NB. Operaciones con índices y filtrado
idx =: 0 2
arr =: 7 8 9 10
idx { arr + 1   NB. resultado: 8 10   NB. 0 2{(7 8 9 10)+1 = 0 2{8 9 10 11 = 8 10

NB. Expresión compleja con varias operaciones
1 + 2 * 3 ^ (1 0 0 1 # 4 5 6 , 7)   NB. resultado: 163 4375

NB. Operaciones con igualdad y negación
0 = 4 + _1 * 2 + 2   NB. resultado: 1   NB. 0=4+((-1)*(2+2)) = 0=4+(-1*4) = 0=4-4 = 1