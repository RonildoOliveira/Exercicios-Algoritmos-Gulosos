### 'Algorismos' Gulosos

Questão 6:
A entrada é uma sequência de números x1, x2, . . . , xn onde n é par. Projete um algoritmo que particione a
entrada em n/2 pares da seguinte maneira. Para cada par, computamos a soma de seus números. Denote por
s1, s2, . . . , sn/2 as n/2 somas. O algoritmo deve encontrar uma partição que minimize a máximo das somas
e deve ser tão eficiente quanto possível. Por exemplo, dados os números (1,3,5,9). As possíveis partições são
{(1,3),(5,9)},{(1,5),(3,9)}, {(1,9),(3,5)}. A soma dos pares para essas partições são (4,14),(6,12) e (10,8). Assim
a terceira partição tem como soma máxima 10 que é o mínimo entre as três partições possíveis. Explique porque
ele funciona e determine a sua complexidade.