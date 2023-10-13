"""
Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores
desse número, com exceção dele próprio. Ex: a soma dos divisores do número 66 é
1 + 2 + 3 + 6 + 11 + 22 + 33 = 78
"""

N = int(input("Digite um número positivo: "))
T = 0

if N > 0:
    print(f"Divisores de {N}:")
    for i in range(1, N + 1):
        if N % i == 0:
            T += i
            print(i)
else:
    print("Esse número não é um número positivo")

print(f"A soma dos divisores é {T}")