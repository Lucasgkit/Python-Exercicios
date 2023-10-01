"""
Exercicio 53: Faça um programa para ler as dimensões de um terreno (comprimento e largura), bem como
o preço do metro da tela. Imprima o custo para cercar esse mesmo terreno com tela.
"""

print("Vamos calcular quanto custara para cercar esse terreno com tela")
print("Qual o comprimento do terreno?")
while True:
    try:
        C = float(input())
        if not 0 <= C <= 10000000000:
            raise ValueError("Número muito grande tente outro.")
    except ValueError as e:
        print("Valor inválido, por favor digite apenas numeros.")
    else:
        break

print("Qual a largura do terreno?")
while True:
    try:
        L = float(input())
        if not 0 <= L <= 10000000000:
            raise ValueError("Número muito grande tente outro.")
    except ValueError as e:
        print("Valor inválido, por favor digite apenas numeros.")
    else:
        break

print("Qual o valor do metro da tela?")
while True:
    try:
        VT = float(input())
        if not 0 <= VT <= 10000000000:
            raise ValueError("Número muito grande tente outro.")
    except ValueError as e:
        print("Valor inválido, por favor digite apenas numeros.")
    else:
        break

AT = L * C
AC = AT * VT

print(f"O Terreno tem {AT:.2f}m² e custará R${AC:.2f} para cobrir com tela")
