"""
Exercicio 7: Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua média.
"""

S = 0
C = 0

for i in range(10):
    N = int(input(f"Digite o {i + 1}º número inteiro: "))
    if N > 0:
        S += N
        C += 1

if C > 0:
    M = S / C
    print(f"A média dos números positivos é: {M}")
else:
    print("Nenhum número positivo foi digitado.")
