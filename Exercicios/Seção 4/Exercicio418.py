"""
Exercicio 16: Leia um valor de volume em metros cúbicos m³ e apresente-o convertido em litros.
"""

print("Vamos fazer uma conversão de metros cúbicos para litros.")
print("Digite quantos metros cúbicos quer converter?")
while True:
    try:
        MB = float(input())
        if not -10000 <= MB <= 10000:
            raise ValueError("Este numero é muito grande por favor digite um numero menor.")
    except ValueError as e:
        print("Valor inválido, por favor digite apenas numeros.")
    else:
        break

L = 1000 * MB
print(f"A conversão resultou em {L:.2f}L.")
