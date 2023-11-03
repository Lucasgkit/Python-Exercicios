"""
Exercicio 48: Faça um programa que some os termos de valor par da sequência de Fibonacci, cujos
valores não ultrapassem quatro milhões.
"""

a, b = 1, 1

S = 0

while a <= 4000000:
    if a % 2 == 0:
        S += a
    a, b = b, a + b

print("A soma dos termos pares da sequência de Fibonacci até 4 milhões é:", S)
