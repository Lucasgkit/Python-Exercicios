"""
Exercicio 31: Faça um prorama que receba a altura e o peso de uma pessoa. De acordo com a tabela
a seguir, verifique e mostre qual classificação dessa pessoa.
Altura          |           Peso
                | até 60 | Entre 60 e 90 | Acima de 90
Menor que 1,20  |   A    |      D        |      G
De 1,20 a 1,70  |   B    |      E        |      H
Maior que 1,70  |   C    |      F        |      I
"""

print("Vamos ver em qual classificação você se encontra.")
A = float(input("Qual a sua altura? "))
P = float(input("Qual o seu peso? "))

if A < 1.20:
    if P < 60:
        print("Você é classificação A.")
    elif 60 <= P <= 90:
        print("Você é classificação D.")
    else:
        print("Você é classificação G.")
elif 1.20 <= A <= 1.70:
    if P < 60:
        print("Você é classificação B.")
    elif 60 <= P <= 90:
        print("Você é classificação E.")
    else:
        print("Você é classificação H.")
else:
    if P < 60:
        print("Você é classificação C.")
    elif 60 <= P <= 90:
        print("Você é classificação F.")
    else:
        print("Você é classificação I.")
