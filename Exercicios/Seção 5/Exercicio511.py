"""
Exercicio 11: Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela a
soma de todos os seus algarismos. Por exemplo, ao número 251 corresponderá o valor 8 (2 + 5 + 1).
Se o número lido não for maior do que zero, o programa terminará com a mensagem "Número inválido".
"""

print("Digite um número inteiro")
NI = int(input())
if 0 <= NI:
    ...
else:
    print("Número inválido.")
    exit()

R = 0

while NI > 0:
    R = R + NI % 10
    NI = NI // 10

print(f"{R}")
