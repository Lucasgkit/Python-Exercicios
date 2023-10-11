"""
Exercicio 17: Faça um programa que leia um número inteiro positivo N e calcule a soma dos N primeiros
números naturais.
"""

N = int(input("Digite um número inteiro positivo: "))

if N <= 0:
    print("Número inválido.")
else:
    soma = 0
    for i in range(1, N + 1):
        soma += i

    print(f"A soma dos {N} primeiros números naturais é {soma}.")
