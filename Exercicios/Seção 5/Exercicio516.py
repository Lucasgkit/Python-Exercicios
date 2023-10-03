"""
Exercicio 16: Usando switch, escreva um programa que leia um inteiro entre 1 e 12 e imprima o mes.
correspondente a este numero. Isto é, janeiro se 1, fevereiro se 2, e assim por diante.
"""

print("Digite um número de 1 a 12")
D = int(input())

if D == 1:
    print("Janeiro")
elif D == 2:
    print("Fevereiro")
elif D == 3:
    print("Março")
elif D == 4:
    print("Abril")
elif D == 5:
    print("Maio")
elif D == 6:
    print("Junho")
elif D == 7:
    print("Julho")
elif D == 8:
    print("Agosto")
elif D == 9:
    print("Setembro")
elif D == 10:
    print("Outubro")
elif D == 11:
    print("Novembro")
elif D == 12:
    print("Dezembro")
else:
    print("Número invalido")
    exit()
