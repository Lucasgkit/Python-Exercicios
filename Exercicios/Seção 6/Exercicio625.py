"""
Exercicio 25: Faça um programa que some todos os números naturais abaixo de 1000 que são múltiplos de 3 ou 5.
"""

S = 0

for N in range(1, 1000):
    if N % 3 == 0 or N % 5 == 0:
        S += N

print(f"A soma dos múltiplos de 3 ou 5 abaixo de 1000 é: {S}")

