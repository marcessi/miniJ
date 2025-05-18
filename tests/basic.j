NB. ======= ARITMÉTICA BÁSICA Y ARRAYS =======

1 2 3                 NB. resultado: 1 2 3
1 1 1 + 1 2 3         NB. resultado: 2 3 4
1 + 1 2 3             NB. resultado: 2 3 4
5 + 2 * 3             NB. resultado: 11
5 * 2 + 3             NB. resultado: 25
(5 * 2) + 3           NB. resultado: 13
_5 + 3                NB. resultado: _2
_1 * 2 3 4            NB. resultado: _2 _3 _4

10 - 7                NB. resultado: 3
3 * 4                 NB. resultado: 12
10 % 3                NB. resultado: 3
3 | 10                NB. resultado: 1
2 ^ 4                 NB. resultado: 16
2 3 4 * 3             NB. resultado: 6 9 12

NB. ======= OPERACIONES RELACIONALES =======

5 > 3                 NB. resultado: 1
5 < 3                 NB. resultado: 0
5 >= 5                NB. resultado: 1
5 <= 3                NB. resultado: 0
5 = 5                 NB. resultado: 1
5 <> 3                NB. resultado: 1
1 2 3 > 0 2 4         NB. resultado: 1 0 0

NB. ======= OPERACIONES ESPECIALES =======

] 42                  NB. resultado: 42
] 1 2 3 4             NB. resultado: 1 2 3 4
5 , 6 7 8             NB. resultado: 5 6 7 8
2 3 , 4 5 6           NB. resultado: 2 3 4 5 6
# 1 2 3 4 5           NB. resultado: 5
# 1 2                 NB. resultat: 2
# 42                  NB. resultado: 1
1 0 1 1 0 # 5 6 7 8 9 NB. resultado: 5 7 8
1 3 { 5 6 7 8 9       NB. resultado: 6 8
0 2 { 2 3 4           NB. resultat: 2 4
i. 6                  NB. resultado: 0 1 2 3 4 5
+: 2 3 4              NB. resultado: 4 6 8
*: 2 3 4              NB. resultado: 4 9 16
+ / 1 2 3 4 5         NB. resultado: 15
* / 1 2 3 4           NB. resultado: 24
5 | ~ 2               NB. resultado: 1

NB. ======= VARIABLES =======

a =: 1 2 3
b =: 10 20 30
c =: 5
a + b                 NB. resultado: 11 22 33
a + c                 NB. resultado: 6 7 8
a * c                 NB. resultado: 5 10 15
sum =: a + b
sum                   NB. resultado: 11 22 33
a =: 5 5 5            NB. Reasignación
a                     NB. resultado: 5 5 5
double_a =: a + a     NB. resultado: 10 10 10
double_a

NB. ======= DEFINICIONES DE FUNCIONES =======

square =: *:
square 1 2 3 4        NB. resultado: 1 4 9 16
square 1 + i. 3       NB. resultado: 1 4 9

mod2 =: 2 | ]
mod2 i. 5             NB. resultado: 0 1 0 1 0

eq0 =: 0 = ]
eq0 1 0 0 1           NB. resultado: 0 1 1 0

NB. ======= OPERACIONES CON =: (ASIGNACIÓN Y AUTOCOMPARACIÓN) =======

=: 5                  NB. resultado: 1 (verifica que 5 = 5)
=: (2 + 3)            NB. resultado: 1 (verifica que 5 = 5)
b =: (=: 4) + (=: 9)
b                     NB. b vale 2 (suma de dos autocomparaciones)

check_eq =: =:        NB. define función de autocomparación
check_eq 15           NB. resultado: 1 (verifica que 15 = 15)

d =: 8
e =: d = (=: d)       
e                     NB. resultado: 0  NB. (8=(8=8)) = (8 = 1) = 0

NB. ======= COMPOSICIÓN DE FUNCIONES =======

parell =: eq0 @: mod2
parell i. 8           NB. resultado: 1 0 1 0 1 0 1 0

triple =: 3 * ]
squared_triple =: square @: triple
squared_triple 1 2 3  NB. resultado: 9 36 81

inc =: 1 + ]
test =: +/ @: inc @: i.
test 4                NB. resultado: 10

vec =: i. 10
mask =: parell vec
evens =: mask # vec
sum_even =: +/ evens
sum_even              NB. resultado: 20

mask =: vec > 5
mask                  NB. resultado: 0 0 0 0 0 0 1 1 1 1
mask # vec            NB. resultado: 6 7 8 9

seq =: i. 5
sum_sq =: +/ @: square
sum_sq seq            NB. resultado: 30  NB. 0²+1²+2²+3²+4² = 30