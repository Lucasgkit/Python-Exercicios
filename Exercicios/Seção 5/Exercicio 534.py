"""
Exercicio 34: Leia a nota e o número de faltas de um aluno, e escreva seu conceito. De acordo com a
tabela abaixo, quando o aluno tem mais de 20 faltas occore uma redução de conceito.

Nota        |   Conceito (até 20 faltas)    |   Conceito (mais de 20 faltas)
9.0 até 10.0|               A               |               B
7.5 até 8.9 |               B               |               C
5.0 ate 7.4 |               C               |               D
4.0 até 4.9 |               D               |               E
0.0 até 3.9 |               E               |               E
"""

print("Vamos calcular seu conceito")
Nota = float(input("Qual foi a sua nota? "))
Falta = int(input("Quantas faltas você tem? "))

if Falta < 20:
    if 9.0 <= Nota <= 10.0:
        print("Aluno conceito nota A.")
    elif 7.5 <= Nota <= 8.9:
        print("Aluno conceito nota B.")
    elif 5.0 <= Nota <= 7.4:
        print("Aluno conceito nota C.")
    elif 4.0 <= Nota <= 4.9:
        print("Aluno conceito nota D.")
    elif 0 <= Nota <= 3.9:
        print("Aluno conceito nota E.")
    else:
        print("Nota inválida")
else:
    if 9.0 <= Nota <= 10.0:
        print("Aluno conceito nota B.")
    elif 7.5 <= Nota <= 8.9:
        print("Aluno conceito nota C.")
    elif 5.0 <= Nota <= 7.4:
        print("Aluno conceito nota D.")
    elif 4.0 <= Nota <= 4.9:
        print("Aluno conceito nota E.")
    elif 0 <= Nota <= 3.9:
        print("Aluno conceito nota E.")
    else:
        print("Nota inválida")
