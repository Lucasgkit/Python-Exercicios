"""
Exercicio 43: Faça um programa que leia um número indeterminado de idades de individuos (pare
quando for informada a idade 0), e calcule a idade média desse grupo.
"""
S = 0
V = 0
while True:
    I = int(input("Digite sua idade (0 para encerrar): "))
    if I == 0:
        break

    S += I
    V += 1

if V > 0:
    M = S / V
    print(f"A média da idade desse grupo é {M}")
else:
    print("Nenhuma idade inserida.")