"""
Exercicio 18: Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles
e quantas vezes no maior número foi lido. A quantidade de números a serem lidos deve ser fonecida
pelo usuário
"""

Q = int(input("Digite a quantidade de números a serem lidos: "))

if Q <= 0:
    print("Quantidade inválida. Deve ser um número positivo.")
else:
    MN = None
    VL = 0

    for i in range(Q):
        numero = float(input(f"Digite o {i + 1}º número: "))

        if i == 0 or numero > MN:
            MN = numero
            VL = 1
        elif numero == MN:
            VL += 1

    if VL == 1:
        plural = ""
    else:
        plural = "es"

    print(f"O maior número lido foi {MN}, e ele foi lido {VL} vez{plural}.")
