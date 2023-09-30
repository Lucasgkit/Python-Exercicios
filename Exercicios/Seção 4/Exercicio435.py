"""
Exercicio 35: Faça um programa que receba os valores de a e b e calcule o valor da hipotenusa atraves da equação.
Sejam a e b os catetos de um triângulo.
Imprima o resultado dessa opração
hipotenusa = √a²+b²
"""

print("Por favor digite o valor do coteto a")
while True:
    try:
        a = float(input())
        if not -10000 <= a <= 10000:
            raise ValueError("Este numero é muito grande por favor digite um numero menor.")
    except ValueError as e:
        print("Valor inválido, por favor digite apenas numeros.")
    else:
        break

print("Por favor digite o valor do coteto b")
while True:
    try:
        b = float(input())
        if not -10000 <= b <= 10000:
            raise ValueError("Este numero é muito grande por favor digite um numero menor.")
    except ValueError as e:
        print("Valor inválido, por favor digite apenas numeros.")
    else:
        break

resul = (a ** 2 + b ** 2) ** 0.5
print(f"A área desse circulo é {resul:.2f}")
