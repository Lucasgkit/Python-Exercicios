"""
Exercicio 19: Escreva um algoritmo que leia um número inteiro entre 100 e 999 e imprima na saida
cada um dos algarismos que compõem o número
"""

N = int(input("Digite um número inteiro entre 100 e 999: "))

if 100 <= N <= 999:
    NS = str(N)
    for A in NS:
        print(A)
else:
    print("Número fora do intervalo válido.")

