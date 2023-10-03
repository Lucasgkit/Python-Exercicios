"""
Exercicio 18: Faça um programa que mostre ao usuário um menu com 4 opções de operações
matemáticas (as básicas, por exemplo). O usuário escolhe uma das opções e o seu
programa então pede dois valores numéricos e realiza a operação, mostrando o resultado
e saindo.
"""

print("Vamos fazer uma operação matemática, por favor escolha uma:")
print("1. Adiçao")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
E = int(input("Digite a opção desejada: "))
if E < 1 or E > 4:
    print("Opção invalida")
    exit()
else:
    V1 = float(input("Digite o 1º valor: "))
    V2 = float(input("Digite o 2º valor: "))

    if E == 1:
        R = V1 + V2
        print(f"O resultado é {R}")
    if E == 2:
        R = V1 - V2
        print(f"O resultado é {R}")
    if E == 3:
        R = V1 * V2
        print(f"O resultado é {R}")
    if E == 4:
        if V2 == 0:
            print("Não é possivel dividir por zero.")
        else:
            R = V1 / V2
            print(f"O resultado é {R}")
