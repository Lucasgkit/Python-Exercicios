"""
Exercicio 8: Leia uma temperatura em graus Klevin e apresente-a convertida em graus Celsius.
"""

print("Vamos fazer uma conversão de graus Kelvin para Celsius.")
print("Quantos graus Kelvin quer converter?")
while True:
    try:
        K = float(input())
        if not -10000 <= K <= 10000:
            raise ValueError("Este numero é muito grande por favor digite um numero menor.")
    except ValueError as e:
        print("Valor inválido, por favor digite apenas numeros.")
    else:
        break

C = K - 273.15
print(f"A temperatura em graus Celsius é {C:.2f}.")
