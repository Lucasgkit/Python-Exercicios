"""
Exercicio 11: Faça um programa que leia um número inteiro positivo N e imprima todos os números
naturais de 0 até N em ordem crescente.
"""

C = 0
N = int(input("Digite um número inteiro positivo: "))
if N < 0:
    print("Número invalido")
    exit()
else:
    while C <= N:
        print(C)
        C += 1
