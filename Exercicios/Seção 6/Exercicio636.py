"""
Exercicio 36: Faça um programa que calcule a diferença entre a soma dos quadrados dos primeiros
100 números naturais e o quadrado da soma.
Ex: A soma dos quadrados dos dez primeiros números naturais é: 1² + 2² + ... + 10² = 385
O quadrado da soma dos dez primeiros números naturais é: ( 1 + 2 + ... + 10)² = 552 = 3025
A diferença entre a soma dos quadrados dos dez primeiros números naturais e o quadrado
da soma é 3025 - 385 = 2640
"""

SQ = 0
SN = 0

for N in range(1, 101):
    SQ += N ** 2
    SN += N

QS = SN ** 2

D = QS - SQ

print(f"A diferença entre a soma dos quadrados e o quadrado da soma dos primeiros 100 números naturais é {D}.")
