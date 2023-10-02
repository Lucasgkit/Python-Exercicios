"""
Exercicio 10: Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu
peso ideal, utilizando as seguintes fórmulas (onde h corresponde á altura):
- Homens: (72.7 * h) - 58
- Mulheres: (62.1 * h) - 4.7
"""

print("Vamos medir seu peso ideal")
print("Você é homem ou mulher?")
S = str(input())
if S == "homem":
    ...
elif S == "mulher":
    ...
else:
    print("Esta resposta não é valida.")
    exit()

print("Qual a sua altura?")
H = float(input())

if S == "homem":
    R = (72.7 * H) - 58
else:
    R = (62.1 * H) - 44.7

print(f"Seu peso ideal é {R:.2f}Kg")
