"""
Exercicio 39: Faça um programa que calcule a área de um triângulo, cuja base e altura são fornecidas
pelo usuário. Esse programa não pode permitir a entrada de dados invàlidos, ou seja, medidas menores
ou iguais a 0.
"""

while True:
    try:
        B = float(input("Digite a base do triângulo: "))
        A = float(input("Digite a altura do triângulo: "))
        if B > 0 and A > 0:
            break
        else:
            print("Base e altura devem ser maiores que zero. Tente novamente.")
    except ValueError:
        print("Por favor, insira um número válido para base e altura.")

AR = 0.5 * B * A

print(f"A área do triângulo é: {AR}")
