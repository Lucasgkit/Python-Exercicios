"""
Exercicio 28: Faça um programa que leia três números inteiros positivos e efetue o cálculo de uma das
seguintes médias de acordo com um valor numérico digitado pelo usuário:
(a) Geométrica: (x * y * Z) \ (1/3)
(b) Ponderada: (x + 2 * y + 3 * z) / 6
(c) Harmônica: 1 / (1/x + 1/y + 1/z)
(d) Aritmética: (x + y + z) /3
"""

print("Escolha uma opção abaixo:")
print("1. Geométrica")
print("2. Ponderada")
print("3. Harmônica")
print("4. Aritmética")
O = int(input())

if O < 1 or O > 4:
    print("Valor invalido")
    exit()
else:
    V1 = int(input("Digite um valor inteiro: "))
    V2 = int(input("Digite um valor inteiro: "))
    V3 = int(input("Digite um valor inteiro: "))

    if O == 1:
        R = (V1 * V2 * V3) / (1/3)
        print(f"Média Geométrica: {R}")
    elif O == 2:
        R = (V1 + 2 * V2 + 3 * V3) / 6
        print(f"Média Ponderada: {R}")
    elif O == 3:
        R = 1 / (1/V1 + 1/V2 + 1/V3)
        print(f"Média Harmônica: {R}")
    else:
        R = (V1 + V2 + V3) / 3
        print(f"Média Aritmética: {R}")
