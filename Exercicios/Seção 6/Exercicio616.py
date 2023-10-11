"""
Exercicio 16: Faça um programa que leia um número inteiro positivo impar N e imprima todos os
números impares de 1 até N em ordem decrescente.
"""

N = int(input("Digite um número inteiro positivo ímpar: "))

if N <= 0 or N % 2 == 0:
    print("Número inválido.")
else:
    C = 1
    while C <= N:
        print(C)
        C += 2


