"""
Exercicio 36: Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro.
"""

print("Por favor digite o valor do raio do cilindro")
while True:
    try:
        R = float(input())
        if not -10000 <= R <= 10000:
            raise ValueError("Este numero é muito grande por favor digite um numero menor.")
    except ValueError as e:
        print("Valor inválido, por favor digite apenas numeros.")
    else:
        break

print("Por favor digite o valor da altura do cilindro")
while True:
    try:
        A = float(input())
        if not -10000 <= A <= 10000:
            raise ValueError("Este numero é muito grande por favor digite um numero menor.")
    except ValueError as e:
        print("Valor inválido, por favor digite apenas numeros.")
    else:
        break

resul = 3.14 * (R ** 2) * A
print(f"O volume desse cilindro é {resul:.2f}")
