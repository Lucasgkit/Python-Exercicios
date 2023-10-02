"""
Exercicio 8: Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas e
exiba na tela a média destas notas. Uma nota válida deve ser, obrigatoriamente, um valor entre
0.0 e 10.0, onde caso a nota não possua um valor válido, este fato deve ser informado ao
usuário e o programa termina.
"""

print("Vamos calcular a sua media")
print("Digite a primeira nota")
N1 = float(input())

if 0 <= N1 <= 10:
    print("Nota computada")
else:
    print(f"Nota invalida")
    exit()

print("Digite a segunda nota")
N2 = float(input())

if 0 <= N2 <= 10:
    print("Nota computada")
else:
    print(f"Nota invalida")
    exit()

M = (N1 + N2) / 2

print(f"Sua média é {M}")
