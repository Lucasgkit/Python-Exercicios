"""
Exercicio 20: Ler uma sequência de números inteiros e determinar se eles são pares ou não. Deverá
ser informado o número de dados lidos e número de valores pares. O processo termina quando for
digitado o número 1000.
"""

NP = 0
NL = 0

while True:
    N = input("Digite um número inteiro (ou '1000' para sair): ")

    if N == '1000':
        break

    NL += 1
    N = int(N)

    if N % 2 == 0:
        NP += 1

print(f"Total de números lidos: {NL}")
print(f"Total de valores pares: {NP}")
