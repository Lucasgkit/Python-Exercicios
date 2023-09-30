"""
Exercicio 40: Uma empresa contrata um encanador a R$ 30,00 por dia.
Faça um programa que solicite o número de dias trabalhados pelo encanador e imprima
a quantia liquida que deverá ser paga, sabendo-se que são descontados 8% para imposto de renda.
"""

print("Vamos calcular quanto o senhor encanador deve receber")
print("Por favor infome quantos dias foram trabalhados")
while True:
    try:
        D = float(input())
        if not -10000 <= D <= 10000:
            raise ValueError("Isso é um exagero meu senhor encanador por favor fale serio.")
    except ValueError as e:
        print("Desculpa mas digite apenas numeros ok?")
    else:
        break

SB = 30 * D
IR = (SB/100) * 8
SL = SB - IR

print(f"O salario liquido do senhor é R${SL:.2f}")
