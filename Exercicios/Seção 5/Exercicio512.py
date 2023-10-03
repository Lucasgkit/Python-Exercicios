"""
Exercicio 12: Ler um número inteiro. Se o número lido for negativo, escreva a mensagem "número inválido".
Se o número for positivo, calcular o logaritmo deste número.
"""

import math

print("Por favor digite um número inteiro")
N = int(input())

if N > 0:
    R = math.log(N)
    print(f"O log de {N} é {R:.2f}")
else:
    print("Número inválido")
