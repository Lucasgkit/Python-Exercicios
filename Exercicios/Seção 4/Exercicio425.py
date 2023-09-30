"""
Exercicio 25: Leia um valor de área em acres e apresente-o convertido em metros quadrados m².
"""

print("Vamos fazer uma conversão de acres para metros quadrados.")
print("Digite quantos acres quer converter?")
while True:
    try:
        A = float(input())
        if not -10000 <= A <= 10000:
            raise ValueError("Este numero é muito grande por favor digite um numero menor.")
    except ValueError as e:
        print("Valor inválido, por favor digite apenas numeros.")
    else:
        break

M = A * 4048.58
print(f"A conversão resultou em {M:.2f}m².")
