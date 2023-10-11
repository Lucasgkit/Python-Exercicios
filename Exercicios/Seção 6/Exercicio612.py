"""
Exercicio 12: Faça um programa que leia um número inteiro positivo N e imprima todos os números
naturais de 0 até N em ordem decrescente.
"""

N = int(input("Digite um número inteiro positivo: "))

if N < 0:
    print("Número inválido")
else:
    C = N
    while C >= 0:
        print(C)
        C -= 1

