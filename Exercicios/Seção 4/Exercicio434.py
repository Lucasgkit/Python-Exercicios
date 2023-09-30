"""
Exercicio 34: Leia o valor do raio de um circulo e calcule e imprima a área do circulo correspondente.
"""

print("Por favor digite o valor de um raio de um circulo")
while True:
    try:
        R = float(input())
        if not -10000 <= R <= 10000:
            raise ValueError("Este numero é muito grande por favor digite um numero menor.")
    except ValueError as e:
        print("Valor inválido, por favor digite apenas numeros.")
    else:
        break

resul = 3.14 * R ** 2
print(f"A área desse circulo é {resul:.2f}")
