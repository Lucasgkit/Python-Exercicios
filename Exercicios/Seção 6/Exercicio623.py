"""
Exercicio 23: Faça um algoritmo que leia um número positivo e imprima seus divisores
"""

N = int(input("Digite um número positivo: "))

if N <= 0:
    print("O número não é positivo.")
else:
    print(f"Divisores de {N}:")
    for i in range(1, N + 1):
        if N % i == 0:
            print(i)
