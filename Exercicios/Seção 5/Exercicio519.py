"""
Exercicio 19: Faça um programa para verificar se um determinado número inteiro é divisivel por 3 ou 5,
mas não simultaneamente pelos dois.
"""

N = int(input("Digite um número inteiro: "))
N3 = N % 3
N5 = N % 5

if (N3 == 0 or N5 == 0) and not (N3 == 0 and N5 == 0):
    print("É divisivel por 3 ou 5.")
elif N3 == 0 and N5 == 0:
    print("É divisivel por 3 e 5 ao mesmo tempo.")
else:
    print("Não é divisivel por 3 ou 5.")
