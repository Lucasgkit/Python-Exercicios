"""
Exercicio 41: Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas
trabalhadas no mes. Imprima o valor a ser pago ao funcionário, adicionando 10% sobre o valor calculado
"""

print("Vamos calcular quanto você deve receber")
print("Por favor infome quanto vale sua hora de trabalho")
while True:
    try:
        V = float(input())
        if not -10000 <= V <= 10000:
            raise ValueError("Este numero é muito grande por favor digite um numero menor.")
    except ValueError as e:
        print("Valor inválido, por favor digite apenas numeros.")
    else:
        break

print("Por favor infome quantas horas foram trabalhados no mes")
while True:
    try:
        H = float(input())
        if not -10000 <= H <= 10000:
            raise ValueError("Este numero é muito grande por favor digite um numero menor.")
    except ValueError as e:
        print("Valor inválido, por favor digite apenas numeros.")
    else:
        break

S = V * H
B = (S/100) * 10
SB = S + B

print(f"Seu salario fica R${S:.2f}, porem você ganhou um bonus de 10%")
print(f"Com o bonus seu salario fica R${SB:.2f}")
