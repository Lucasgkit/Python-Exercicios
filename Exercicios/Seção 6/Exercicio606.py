"""
Exercicio 6: Faça um programa que leia 10 inteiros e imprima sua média.
"""

S = 0

for i in range(10):
    N = int(input(f"Digite o {i + 1}º número inteiro: "))
    S += N

M = S / 10

# Exiba a média
print(f"A média dos 10 números é: {M}")

