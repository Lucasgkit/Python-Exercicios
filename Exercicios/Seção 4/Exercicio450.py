"""
Exercicio 50: Implemente um programa que calcule o ano de nascimento de uma pessoa a partir
de sua idade e do ano atual.
"""

print("Qual a sua idade?")
while True:
    try:
        I = int(input())
        if not 0 <= I <= 10000000000:
            raise ValueError("Número muito grande tente outro.")
    except ValueError as e:
        print("Valor inválido, por favor digite apenas numeros.")
    else:
        break

print("Em que ano estamos?")
while True:
    try:
        A = int(input())
        if not 0 <= A <= 10000000000:
            raise ValueError("Número muito grande tente outro.")
    except ValueError as e:
        print("Valor inválido, por favor digite apenas numeros.")
    else:
        break

print("Já fez aniversario esse ano?")
print("Digite '0' para sim ou '1' para não")
while True:
    try:
        Niver = int(input())
        if not 0 <= Niver <= 1:
            raise ValueError("Número muito grande tente outro.")
    except ValueError as e:
        print("Valor inválido, por favor digite apenas numeros.")
    else:
        break

N = A - I
AN = N - Niver

print(f"Você nasceu em {AN}")
