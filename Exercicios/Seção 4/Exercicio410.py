"""
Exercicio 8: Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin.
"""

print("Vamos fazer uma conversão de graus Celsius para Kelvin.")
print("Quantos graus Celsius quer converter?")
while True:
    try:
        C = float(input())
        if not -10000 <= C <= 10000:
            raise ValueError("Este numero é muito grande por favor digite um numero menor.")
    except ValueError as e:
        print("Valor inválido, por favor digite apenas numeros.")
    else:
        break

K = C + 273.15
print(f"A temperatura em graus Kelvin é {K:.2f}.")
