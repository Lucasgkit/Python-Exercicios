"""
Exercicio 37: Escreva um programa que verifique quais números entre 1000 e 9999 (inclusive) possuem
a propriedade seguinte: a soma dos dois digitos de mais baixa ordem com os dois digitos de mais alta
ordem elevada ao quadrado é igual ao próprio numero. Por exemplo, para o inteiro 3025, temos que:
30 + 25 = 55
55² = 3025
"""

for N in range(1000, 10000):
    P1 = N // 100
    P2 = N % 100
    SP = P1 + P2
    SPQ = SP ** 2

    if SPQ == N:
        print(N)
