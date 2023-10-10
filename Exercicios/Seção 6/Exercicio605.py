"""
Exercicio 5: Faça um programa que peça ao usuário para digitar 10 valores e some-os
"""

S = 0

for i in range(10):
    V = float(input(f"Digite o {i + 1}º valor: "))
    S += V

print(f"A soma dos 10 valores é: {S}")
