"""
Exercicio 31: Faça um programa que calcule e escreva o valor de S.
S = 1/1 + 3/2 + 5/3 + 7/4 ... 99/50
"""

S = 0
D = 1

for N in range(1, 100, 2):
    S += N / D
    D += 1

print(f"O valor de S é {S:.2f}")
