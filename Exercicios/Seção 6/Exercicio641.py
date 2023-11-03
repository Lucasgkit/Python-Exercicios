"""
Exercicio 41: Faça um programa que calcula a associação em paralelo de dois resistores R1 e R2
fornecidos pelo usuário via teclado. O programa fica pedindo estes valores e calculando até que
o usuário entre com um valor para resistência igual a zero.
R = (R1 * R2) / (R1 + R2)
"""

while True:
    R1 = float(input("Digite o valor de R1 (ou 0 para sair): "))
    if R1 == 0:
        break

    R2 = float(input("Digite o valor de R2 (ou 0 para sair): "))
    if R2 == 0:
        break

    R = (R1 * R2) / (R1 + R2)

    print(f"A resistência em paralelo de R1 = {R1} e R2 = {R2} é: {R}")
