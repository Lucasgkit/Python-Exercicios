"""
Exercicio 12: Leia uma distancia em quilômetros e apresente-a convertida em milhas.
"""

print("Vamos fazer uma conversão de quilômetros para milhas.")
print("Quantos quilômetros quer converter?")
while True:
    try:
        K = float(input())
        if not -10000 <= K <= 10000:
            raise ValueError("Este numero é muito grande por favor digite um numero menor.")
    except ValueError as e:
        print("Valor inválido, por favor digite apenas numeros.")
    else:
        break

M = K / 1.61
print(f"A distância em milhas é de {M:.2f} milhas.")
