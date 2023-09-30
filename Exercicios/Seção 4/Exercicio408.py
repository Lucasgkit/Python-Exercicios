"""
Exercicio 7: Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
"""

print("Vamos fazer uma conversão de graus Fahrenheit para Celsius.")
print("Quantos graus Fahrenheit quer converter?")
while True:
    try:
        F = float(input())
        if not -10000 <= F <= 10000:
            raise ValueError("Este numero é muito grande por favor digite um numero menor.")
    except ValueError as e:
        print("Valor inválido, por favor digite apenas numeros.")
    else:
        break

C = 5.0 * (F - 32.0) / 9.0
print(f"A temperatura em graus Fahrenheit é {C:.2f}.")