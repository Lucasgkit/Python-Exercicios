"""
Exercicio 5: Faça um programa que receba um número inteiro e verifique se este número é par ou ímpar.
"""

print("Por favor digite um número inteiro")
N = int(input())
D = N % 2

if D == 0:
    print(f"O número {N} é um número par")
else:
    print(f"O número {N} é impar")
