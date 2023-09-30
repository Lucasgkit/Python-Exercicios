"""
Exercicio 23: Leia um valor de comprimento em metros e apresente-o convertido em jardas.
"""

print("Vamos fazer uma conversão de metros para jardas.")
print("Digite quantos metros quer converter?")
while True:
    try:
        M = float(input())
        if not -10000 <= M <= 10000:
            raise ValueError("Este numero é muito grande por favor digite um numero menor.")
    except ValueError as e:
        print("Valor inválido, por favor digite apenas numeros.")
    else:
        break

J = M / 0.91
print(f"A conversão resultou em {J:.2f} jardas.")
