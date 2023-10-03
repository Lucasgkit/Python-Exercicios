"""
Exercicio 15: Usando switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia
da semana correspondente a este numero. Isto é, domingo se 1, segunda-feira se 2, e assim por diante.
"""

print("Digite um número de 1 a 7")
D = int(input())

if D == 1:
    print("Domingo")
elif D == 2:
    print("Segunda-feira")
elif D == 3:
    print("Terça-feira")
elif D == 4:
    print("Quarta-feira")
elif D == 5:
    print("Quinta-feira")
elif D == 6:
    print("Sexta-feira")
elif D == 7:
    print("Sabado")
else:
    print("Número invalido")
    exit()
