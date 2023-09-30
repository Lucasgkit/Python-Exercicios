"""
Exercicio 37: Faça um programa que leia o valor de um produto e imprima o valor com desconto,
tendo em vista que o desconto foi de 12%
"""

print("Por favor digite o valor do produto que receba o desconto de 12%")
while True:
    try:
        P = float(input())
        if not -10000 <= P <= 10000:
            raise ValueError("Este numero é muito grande por favor digite um numero menor.")
    except ValueError as e:
        print("Valor inválido, por favor digite apenas numeros.")
    else:
        break
D = (P/100) * 12
resul = P - D
print(f"O produto com desconto ficou {resul:.2f}")
