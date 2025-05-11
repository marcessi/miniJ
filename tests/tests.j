1 2 3 + _1 _2 _3    NB. resultat: 2 3 4
1 _2 3        NB. resultat: 2 3 4
5 + 2 * 3        NB. resultat: 11
5 * 2 + 3        NB. resultat: 25
(5 * 2) + 3      NB. resultat: 13
_1 * 2 3         NB. resultat: _2 _3
5 - 2            NB. resultat: 3
2 * 3            NB. resultat: 6
2 * 3 4 5        NB. resultat: 6 8 10
6 % 2            NB. resultat: 3
2 | 7            NB. resultat: 1
2 ^ 3            NB. resultat: 8
_1 * 3 4 5       NB. resultat: _3 _4 _5
(2 + 3) * 4      NB. resultat: 20
2 + 3 * 4        NB. resultat: 14

NB. Operadores relacionales
3 > 2            NB. resultat: 1
3 < 2            NB. resultat: 0
3 >= 3           NB. resultat: 1
3 <= 2           NB. resultat: 0
3 = 3            NB. resultat: 1
3 <> 3           NB. resultat: 0
1 2 3 > 0 2 4    NB. resultat: 1 0 0

NB. Función identidad
] 42             NB. resultat: 42
] 1 2 3          NB. resultat: 1 2 3

NB. Concatenación
1 , 2 3          NB. resultat: 1 2 3
1 2 , 3 4        NB. resultat: 1 2 3 4

NB. Tamaño de vector
# 1 2 3 4 5      NB. resultat: 5
# 42             NB. resultat: 1

NB. Filtro con máscara
1 0 1 0 # 5 6 7 8    NB. resultat: 5 7

NB. Acceso por índice
0 2 { 5 6 7 8    NB. resultat: 5 7
1 { 5 6 7        NB. resultat: 6

NB. Secuencia de números naturales
i. 5             NB. resultat: 0 1 2 3 4

NB. Operadores con : (conversión a unario)
+: 1 2 3         NB. resultat: 2 4 6
*: 2 3 4         NB. resultat: 4 9 16

NB. Fold (reducción)
+ / 1 2 3 4      NB. resultat: 10
* / 1 2 3 4      NB. resultat: 24

NB. Flip (inversión de operandos)
7 | ~ 2          NB. resultat: 1
