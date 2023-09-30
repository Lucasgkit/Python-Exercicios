"""
Exercicio 14: Leia um ângulo em graus e apresente-o convertido em radianos
"""

print("Vamos fazer uma conversão de graus para radianos.")
print("Digite quantos graus quer converter?")
while True:
    try:
        G = float(input())
        if not -10000 <= G <= 10000:
            raise ValueError("Este numero é muito grande por favor digite um numero menor.")
    except ValueError as e:
        print("Valor inválido, por favor digite apenas numeros.")
    else:
        break

R = G * 3.14/180
print(f"O ângulo foi convertido para {R:.2f} radianos.")
