NB. ======= PROCESAMIENTO DE DATOS =======

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

NB. ======= TRANSFORMACIONES EN CADENA =======

NB. Secuencia anidada: (x^2 + 2) * (3 - x)
sq_plus2 =: (] ^ 2) + 2
minus_from3 =: 3 - ]
chain_transform =: sq_plus2 * minus_from3
chain_transform 1 2 3     NB. resultado: 6 6 0  NB. (x^2+2)*(3-x)

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
filtered_nums            NB. resultado: 4 6 8  NB. Elementos pares y > 3
transformed =: double_plus1 filtered_nums
transformed              NB. resultado: 9 13 17
sum_result =: +/ transformed
sum_result               NB. resultado: 39  NB. (2*4+1)+(2*6+1)+(2*8+1) = 9+13+17 = 39

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
mask_fn =: (1 = 2 | ]) * (3 < ])
mask =: mask_fn data
filtered =: mask # data
filtered                 NB. resultado: 5 9  NB. Elementos impares y > 3

NB. Cálculo de polinomio mediante composición: x^3 - 2x^2 + 3x - 1
x3 =: ] ^ 3 
x2 =: ] ^ 2
x1 =: ]
poly =: (x3 - (2 * x2)) + (3 * x1) - 1
poly 1 2 3               NB. resultado: 1 5 17  NB. x^3-2x^2+3x-1