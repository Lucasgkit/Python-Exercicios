"""
Exercicio 11: Leia uma velocidade em m/s e apresente-a convertida em km/h.
"""

print("Vamos converter uma velocidade de Km/h em m/s")
print("Quantos m/s quer converter??")
while True:
    try:
        M = float(input())
        if not -10000 <= M <= 10000:
            raise ValueError("Este numero é muito grande por favor digite um numero menor.")
    except ValueError as e:
        print("Valor inválido, por favor digite apenas numeros.")
    else:
        break

K = M * 3.6
print(f"A conversão foi realizada: {K:.2f}Km/h.")