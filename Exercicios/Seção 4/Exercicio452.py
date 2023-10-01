"""
Exercicio 52: Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido
proporcionalmente ao valor que cada um deu para a realizaçõa da a aposta. Faça um programa
que leia quanto cada apostador investiu, o valor do prêmio, e imprima quanto cada um
ganhar do prêmio com base no valor investido.
"""

print("Quanto você apostou?")
while True:
    try:
        J1 = float(input())
        if not 0 <= J1 <= 10000000000:
            raise ValueError("Número muito grande tente outro.")
    except ValueError as e:
        print("Valor inválido, por favor digite apenas numeros.")
    else:
        break

print("Quanto você apostou?")
while True:
    try:
        J2 = float(input())
        if not 0 <= J2 <= 10000000000:
            raise ValueError("Número muito grande tente outro.")
    except ValueError as e:
        print("Valor inválido, por favor digite apenas numeros.")
    else:
        break

print("Quanto você apostou?")
while True:
    try:
        J3 = float(input())
        if not 0 <= J3 <= 10000000000:
            raise ValueError("Número muito grande tente outro.")
    except ValueError as e:
        print("Valor inválido, por favor digite apenas numeros.")
    else:
        break

print("Quanto é o prêmio?")
while True:
    try:
        P = float(input())
        if not 0 <= P <= 10000000000:
            raise ValueError("Número muito grande tente outro.")
    except ValueError as e:
        print("Valor inválido, por favor digite apenas numeros.")
    else:
        break

aposta = J1 + J2 + J3
PorcentagemJ1 = (J1 * 100) / aposta
PorcentagemJ2 = (J2 * 100) / aposta
PorcentagemJ3 = (J3 * 100) / aposta
PJ1 = (P/100) * PorcentagemJ1
PJ2 = (P/100) * PorcentagemJ2
PJ3 = (P/100) * PorcentagemJ3

print(f"Jogador 1 recebera {PorcentagemJ1:.2f}% do prêmio que é R${PJ1:.2f}")
print(f"Jogador 2 recebera {PorcentagemJ2:.2f}% do prêmio que é R${PJ2:.2f}")
print(f"Jogador 3 recebera {PorcentagemJ3:.2f}% do prêmio que é R${PJ3:.2f}")
