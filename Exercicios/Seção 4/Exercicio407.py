"""
Exercicio 6: Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
"""

print("Vamos fazer uma conversão de graus Celsius para Fahrenheit.")
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

F = C * (9.0/5.0) + 32.0
print(f"A temperatura em graus Fahrenheit é {F:.2f}.")
