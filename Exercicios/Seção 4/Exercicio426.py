"""
Exercicio 26: Leia um valor de área em metros quadrados m² e apresente-o convertido em hectares.
"""

print("Vamos fazer uma conversão de metros quadrados para hectares.")
print("Digite quantos metros quadrados quer converter?")
while True:
    try:
        M = float(input())
        if not -10000 <= M <= 10000:
            raise ValueError("Este numero é muito grande por favor digite um numero menor.")
    except ValueError as e:
        print("Valor inválido, por favor digite apenas numeros.")
    else:
        break

H = M * 0.0001
print(f"A conversão resultou em {H:.2f} hecatres.")
