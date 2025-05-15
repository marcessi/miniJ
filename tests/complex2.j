NB. Test file for miniJ interpreter - ADVANCED FUNCTION COMPOSITION
NB. Pruebas avanzadas para composición funcional y transformaciones

NB. ======= COMPOSICIONES RECURSIVAS Y TRANSFORMACIONES ANIDADAS =======

NB. Fibonacci simplificado 
fib_helper =: ] - 1
fib_recursive =: ] + fib_helper
fib_recursive 5          NB. resultado: 9

NB. Triple transformación: cubo del doble
double =: 2 * ]
cube =: ] ^ 3
transform =: cube @: double
transform 4 9 16   NB. resultado: 512 5832 32768   NB. (2*x)^3

NB. ======= OPERACIONES VECTORIALES COMPUESTAS =======

NB. Vector de distancias al origen simplificado
points =: 3 4 5
squares =: points ^ 2
dist =: +/ squares
dist                   NB. resultado: 50

NB. ======= FILTROS COMBINADOS Y TRANSFORMACIONES =======

NB. Obtener elementos que son múltiplos de 3
numbers =: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
div_by_3 =: 0 = 3 | ]
mask =: div_by_3 numbers
filtered =: mask # numbers
filtered                 NB. resultado: 3 6 9 12 15

NB. ======= PROCESAMIENTO DE DATOS BÁSICO =======

NB. Normalización simple: (x - media)
data =: 10 20 30 40 50
mean =: +/ data % # data
z_simple =: data - mean
z_simple                 NB. resultado: _20 _10 0 10 20

NB. Correlación simplificada
x =: 1 2 3 4 5
y =: 2 3 5 8 11
x_mean =: +/ x % # x
y_mean =: +/ y % # y
x_dev =: x - x_mean
x_dev                    NB. resultado: _2 _1 0 1 2
y_dev =: y - y_mean
y_dev                    NB. resultado: _3 _2 0 3 6
correlation =: +/ (x_dev * y_dev)
correlation              NB. resultado: 23

NB. ======= FUNCIONES DE ORDEN SUPERIOR =======

NB. Suma de pares consecutivos
data =: 1 2 3 4 5
mask1 =: 1 1 1 1 0
mask2 =: 0 1 1 1 1
part1 =: mask1 # data
part2 =: mask2 # data 
pair_sums =: part1 + part2
pair_sums                NB. resultado: 3 5 7 9

NB. Función que suma elementos alternos
alt_data =: 1 2 3 4 5
alt_mask =: 1 0 1 0 1
alt_filtered =: alt_mask # alt_data
skip_sum =: +/ alt_filtered
skip_sum                 NB. resultado: 9  NB. 1 + 3 + 5

NB. ======= TRANSFORMACIONES EN CADENA =======

NB. Secuencia anidada: (x^2 + 2) * (3 - x)
sq_plus2 =: (] ^ 2) + 2
minus_from3 =: 3 - ]
chain_transform =: sq_plus2 @: ] * minus_from3
chain_transform 1 2 3     NB. resultado: 6 6 2  NB. (x^2+2)*(3-x)

NB. ======= COMPOSICIONES MÚLTIPLES COMPLEJAS =======

NB. Filtrar, transformar y agregar en una sola cadena
nums =: i. 10
is_even =: 0 = 2 | ]
is_gt3 =: 3 < ]
double_plus1 =: 1 + 2 * ]
even_mask =: is_even nums
gt3_mask =: is_gt3 nums
combined_mask =: even_mask * gt3_mask
filtered_nums =: combined_mask # nums
transformed =: double_plus1 filtered_nums
transformed              NB. resultado: 9 13 17
sum_result =: +/ transformed
sum_result               NB. resultado: 39  NB. (2*4+1)+(2*6+1)+(2*8+1) = 9+13+17 = 39

NB. Detectar si una secuencia es perfectamente alternante (0,1,0,1...)
sequence =: 0 1 0 1 0 1
expected =: 2 | i. 6
diff =: sequence = expected
matches =: +/ diff
matches                 NB. resultado: 6  NB. Todos los elementos coinciden

NB. Cuádruple composición: elevar al cubo la diferencia del doble con el triple
double =: 2 * ]
triple =: 3 * ]
diff =: double - triple
cube_fn =: ] ^ 3
mega_chain =: cube_fn @: diff
mega_chain 1 2 3 4       NB. resultado: _1 _8 _27 _64  NB. ((2*x)-(3*x))^3 = (-x)^3

NB. Composición con operaciones binarias y unarias mezcladas
square =: *:
inc =: 1 + ]
min5 =: ] < 5
mix_fn =: square @: inc @: (min5 # ])
mix_fn 2 4 6 8           NB. resultado: 9 25  NB. si x<5 entonces (x+1)^2 sino no se añade

NB. Operación de filtrado con máscara generada por composición
data =: 3 1 4 1 5 9 2 6
mask_fn =: (1 = (] @: 2 | ])) * (3 < ])
mask =: mask_fn data
filtered =: mask # data
filtered                 NB. resultado: 5 9  NB. Elementos impares y > 3

NB. Cálculo de polinomio mediante composición: x^3 - 2x^2 + 3x - 1
x3 =: ] ^ 3 
x2 =: ] ^ 2
x1 =: ]
poly =: (x3 - (2 * x2)) + (3 * x1) - 1
poly 1 2 3               NB. resultado: 1 5 17  NB. x^3-2x^2+3x-1