"""
Exercicio 40: Elabore um programa que faça leitura de vários números inteiros, até que se digite um
número negativo. O programa tem que retornar o maior e o menor número lido.
"""

N = int(input("Digite um número inteiro (ou um número negativo para encerrar): "))

MA = N
MI = N

while N >= 0:
    if N > MA:
        MA = N
    if N < MI:
        MI = N

    N = int(input("Digite outro número inteiro (ou um número negativo para encerrar): "))


print(f"O maior número lido é: {MA}")
print(f"O menor número lido é: {MI}")
