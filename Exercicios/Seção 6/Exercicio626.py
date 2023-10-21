"""
Exercicio 26: Faça um algoritmo que encontre o primeiro múltiplo de 11, 13 ou 17 após um número dado.
"""

N = int(input("Digite um número: "))
V = False

while not V:
    N += 1
    if N % 11 == 0 or N % 13 == 0 or N % 17 == 0:
        V = True

print(f"O primeiro múltiplo de 11, 13 ou 17 após o número dado é: {N}")
