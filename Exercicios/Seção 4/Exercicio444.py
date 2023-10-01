"""
Exercicio 44: Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar
subindo a escada. Calcule e mostre quantos degraus o usuário deverá subir para atingir seu objetivo.
"""

print("Qual a altura de cada degrau em cm?")

while True:
    try:
        AD = float(input())
        if not -10000000 <= AD <= 10000000:
            raise ValueError("Este numero é muito grande por favor digite um numero menor.")
    except ValueError as e:
        print("Valor inválido, por favor digite apenas numeros.")
    else:
        break

print("Qual a altura que deseja alcançar em metros?")

while True:
    try:
        AL = float(input())
        if not -10000000 <= AL <= 10000000:
            raise ValueError("Este numero é muito grande por favor digite um numero menor.")
    except ValueError as e:
        print("Valor inválido, por favor digite apenas numeros.")
    else:
        break

ADM = AD/100
TD = AL/ADM

print(f"Você precisara subir {TD:.2f} degraus para atingir {AL:.2f} metros")
