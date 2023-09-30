"""
Exercicio 27: Leia um valor de área em hectares e apresente-o convertido em metros quadrados m².
"""

print("Vamos fazer uma conversão de hectares para metros quadrados.")
print("Digite quantos hectares quer converter?")
while True:
    try:
        H = float(input())
        if not -10000 <= H <= 10000:
            raise ValueError("Este numero é muito grande por favor digite um numero menor.")
    except ValueError as e:
        print("Valor inválido, por favor digite apenas numeros.")
    else:
        break

M = H * 10000
print(f"A conversão resultou em {M:.2f}m².")
