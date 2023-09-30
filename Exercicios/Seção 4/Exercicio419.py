"""
Exercicio 19: Leia um valor de volume em litros e apresente-o convertido em metros cúbicos m³.
"""

print("Vamos fazer uma conversão de metros cúbicos para litros.")
print("Digite quantos metros cúbicos quer converter?")
while True:
    try:
        L = float(input())
        if not -10000 <= L <= 10000:
            raise ValueError("Este numero é muito grande por favor digite um numero menor.")
    except ValueError as e:
        print("Valor inválido, por favor digite apenas numeros.")
    else:
        break

MB = L / 1000
print(f"A conversão resultou em {MB:.2f}m³.")
