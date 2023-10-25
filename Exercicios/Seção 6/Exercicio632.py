"""
Exercicio 32: Faça um programa que simula o lançamneto de dois dados D1 e D2, n vezes, e tem como
saida o número de cada dado e a relação entre eles (>,<,=) de cada lançamento
"""

import random

NL = int(input("Digite o número de lançamentos desejado: "))

for _ in range(NL):
    D1 = random.randint(1, 6)
    D2 = random.randint(1, 6)

    if D1 > D2:
        R = "Dado 1 é maior que o Dado 2"
    elif D1 < D2:
        R = "Dado 2 é maior que o Dado 1"
    else:
        R = "Dado 1 é igual o Dado 2"

    print(f"Lançamento: D1= {D1}, D2= {D2}, Relação: {R}")
