"""
Exercicio 12: Leia uma distancia em milhas e apresente-a convertida em quilômetros.
"""

print("Vamos fazer uma conversão de milhas para quilômetros.")
print("Quantas milhas quer converter?")
while True:
    try:
        M = float(input())
        if not -10000 <= M <= 10000:
            raise ValueError("Este numero é muito grande por favor digite um numero menor.")
    except ValueError as e:
        print("Valor inválido, por favor digite apenas numeros.")
    else:
        break

K = 1.61 * M
print(f"A distância em quilômetros é de {K:.2f}Km.")
