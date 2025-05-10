NB. Variables y asignación - Ejemplos ampliados

NB. Asignaciones básicas
x =: 1 2 3
y =: 10 20 30
z =: 5

NB. Operaciones con variables
1 + x        NB. resultat: 2 3 4
x + y        NB. resultat: 11 22 33
x * y        NB. resultat: 10 40 90

NB. Asignación de resultados de expresiones
sum =: x + y       NB. Guarda 11 22 33
prod =: x * y      NB. Guarda 10 40 90

NB. Verificación de variables almacenadas
sum            NB. Comprobar que sum contiene: 11 22 33
prod           NB. Comprobar que prod contiene: 10 40 90

NB. Operaciones con el resultado
sum + prod         NB. resultat: 21 62 123

NB. Reasignación de variables
x =: 5 5 5
x              NB. Verificar que x ahora es: 5 5 5
x + y          NB. resultat: 15 25 35

NB. Variables que usan otras variables
double_x =: x + x  NB. Guarda 10 10 10
double_x          NB. Verificar double_x

NB. Operadores especiales
len =: #x          NB. Tamaño de x: 3
len               NB. Verificar que len es 3
seq =: i.5         NB. Secuencia de 0 a 4
seq              NB. Verificar que seq es 0 1 2 3 4
concat =: x,y      NB. Concatenación: 5 5 5 10 20 30
concat           NB. Verificar concat

NB. Cadena de reasignaciones
temp =: x          NB. temp = 5 5 5
x =: y            NB. x = 10 20 30
y =: temp         NB. y = 5 5 5
x                NB. Verificar que x = 10 20 30
y                NB. Verificar que y = 5 5 5

NB. Filtrado y acceso
mask =: x > 15     NB. Máscara: 0 1 1 
mask              NB. Verificar máscara
filtered =: mask#y NB. Elementos de y donde mask es 1: 5 5
filtered          NB. Verificar filtered

NB. Reutilización de variables
count =: +/mask    NB. Suma de elementos en la máscara (cuántos son verdaderos)
count             NB. Debe ser 2

NB. Operaciones incrementales
running_sum =: 0   NB. Inicializar contador
running_sum =: running_sum + x      NB. Añadir x
running_sum                         NB. Verificar: 10 20 30
running_sum =: running_sum + y      NB. Añadir y
running_sum                         NB. Verificar: 15 25 35

NB. Operaciones más complejas
a =: 2
b =: 3
c =: a^b           NB. Potencia: 8
c                 NB. Verificar c
d =: +:b          NB. Operador modificado: 6 (3+3)
d                 NB. Verificar d
e =: +/x           NB. Fold (suma): 60
e                 NB. Verificar e
f =: x*~y          NB. Operación flipped: 50 100 150
f                 NB. Verificar f

NB. Variables en expresiones anidadas
result =: (x + y) * z    NB. (10 20 30 + 5 5 5) * 5
result                  NB. Verificar que es 75 125 175
size =: #result         NB. Tamaño del resultado
size                    NB. Verificar que es 3

NB. Operaciones relacionales
cmp1 =: x = 10     NB. Comparación igual: 1 0 0
cmp1               NB. Verificar cmp1
cmp2 =: y > 4      NB. Mayor que: 1 1 1
cmp2               NB. Verificar cmp2
all_equal =: +/cmp1  NB. Suma de comparaciones: 1
all_equal           NB. Verificar all_equal

NB. Composición de operaciones con variables
squares =: x * x         NB. Cuadrados de x: 100 400 900
squares                 NB. Verificar squares
cube =: squares * x      NB. Cubos de x: 1000 8000 27000
cube                    NB. Verificar cube

NB. Variables como acumuladores
counter =: 0
counter =: counter + 1    NB. Incrementa contador
counter =: counter + 1    NB. Incrementa contador otra vez
counter                  NB. Verificar que counter es 2

NB. Manipulación avanzada
indices =: i.#x          NB. 0 1 2
doubled =: 2 * x         NB. 20 40 60
combined =: indices + doubled  NB. 20 41 62
combined                      NB. Verificar combined
