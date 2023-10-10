"""
Exercicio 10: Faça um programa que calcule e mostre a soma dos 50 primeiros números pares.
"""

S = 0

for N in range(2, 101, 2):
    S += N

print("A soma dos 50 primeiros números pares é:", S)
