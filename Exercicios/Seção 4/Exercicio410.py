"""
Exercicio 10: Leia uma velocidade em km/h e apresente-a convertida em m/s.
"""

print("Vamos converter uma velocidade de Km/h em m/s")
print("Quantos Km/h quer converter??")
while True:
    try:
        K = float(input())
        if not -10000 <= K <= 10000:
            raise ValueError("Este numero é muito grande por favor digite um numero menor.")
    except ValueError as e:
        print("Valor inválido, por favor digite apenas numeros.")
    else:
        break

M = K / 3.6
print(f"A conversão foi realizada: {M:.2f}m/s.")