"""
Exercicio 8: Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido.
"""

N1 = float(input("Digite o 1º número: "))
ME = N1
MA = N1

for i in range(2, 11):
    N = float(input(f"Digite o {i}º número: "))
    if N < ME:
        ME = N
    if N > MA:
        MA = N

print(f"O menor valor digitado é: {ME}")
print(f"O maior valor digitado é: {MA}")
