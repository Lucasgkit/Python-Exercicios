"""
Exercicio 46: Faça um programa que gera um número aleatório de 1 a 1000. O usuário deve tentar
acertar qual numero foi gerado, a cada tentativa o programa deverá informar se o chute é menor
ou maior que o número gerado. O programa acaba quando o usuário acertar o número gerado. O programa
deve informar em quantas tentativas o número foi descoberto.
"""

import random

N = random.randint(1, 1000)

V = 0
A = False

while not A:
    T = int(input("Tente adivinhar o número entre 1 e 1000: "))
    V += 1

    if T == N:
        A = True
        print(f"Parabéns! Você acertou o número {N} em {V} tentativas.")
    elif T < N:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")
