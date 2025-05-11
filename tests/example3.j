1 2 3                NB. resultado: 1 2 3
1 1 1 + 1 2 3        NB. resultado: 2 3 4
1 + 1 2 3            NB. resultado: 2 3 4

5 + 2 * 3            NB. resultado: 11
5 * 2 + 3            NB. resultado: 25
(5 * 2) + 3          NB. resultado: 13

_1 * 2 3             NB. resultado: _2 _3

5 - 2                NB. resultado: 3
_5                  NB. resultado: -5
2 * 3                NB. resultado: 6
6 % 2                NB. resultado: 3
2 | 7                NB. resultado: 1
2 ^ 3                NB. resultado: 8

1 > 0                NB. resultado: 1
1 < 0                NB. resultado: 0
1 >= 1               NB. resultado: 1
1 <= 0               NB. resultado: 0
1 = 1                NB. resultado: 1
1 <> 0               NB. resultado: 1

] 1                  NB. resultado: 1
1 , 2 3              NB. resultado: 1 2 3
# 1 2                NB. resultado: 2
1 0 1 0 # 1 2 3 4    NB. resultado: 1 3
0 2 { 2 3 4          NB. resultado: 2 4
i. 4                 NB. resultado: 0 1 2 3

+: 1 2 3             NB. resultado: 2 4 6
+ / 1 2 3            NB. resultado: 6
7 | ~ 2              NB. resultado: 1

x =: 1 2 3
1 + x                NB. resultado: 2 3 4

square =: *:
square 1 2 3 4       NB. resultado: 1 4 9 16

mod2 =: 2 | ]
mod2 i. 4            NB. resultado: 0 1 0 1

eq0 =: 0 = ]
parell =: eq0 @: mod2
parell i. 6          NB. resultado: 1 0 1 0 1 0

square =: *:
square 1 + i. 3      NB. resultado: 1 4 9

mod2 =: 2 | ]
eq0 =: 0 = ]
eq0 mod2 i. 6        NB. resultado: 1 0 1 0 1 0

parell =: eq0 @: mod2
parell i. 6          NB. resultado: 1 0 1 0 1 0

parell =: 0 = ] @: 2 | ]
parell i. 6          NB. resultado: 1 0 1 0 1 0

inc =: 1 + ]
test =: +/ @: inc @: i.
test 3               NB. resultado: 6
