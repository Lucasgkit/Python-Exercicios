"""
Exercicio 9: Faça um programa que leia um número inteiro N e depois imporima os N primeiros
números naturais impares.
"""

N = int(input("Digite um número inteiro N: "))

C = 1

for _ in range(N):
    print(C)
    C += 2
