"""
Exercicio 22: Leia um valor de comprimento em jardas e apresente-o convertido em metros.
"""

print("Vamos fazer uma conversão de jardas para metros.")
print("Digite quantas jardas quer converter?")
while True:
    try:
        J = float(input())
        if not -10000 <= J <= 10000:
            raise ValueError("Este numero é muito grande por favor digite um numero menor.")
    except ValueError as e:
        print("Valor inválido, por favor digite apenas numeros.")
    else:
        break

M = 0.91 * J
print(f"A conversão resultou em {M:.2f}m.")
