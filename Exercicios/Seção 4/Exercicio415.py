"""
Exercicio 15: Leia um ângulo em radianos e apresente-o convertido em graus.
"""

print("Vamos fazer uma conversão de radianos para graus.")
print("Digite quantos radianos quer converter?")
while True:
    try:
        R = float(input())
        if not -10000 <= R <= 10000:
            raise ValueError("Este numero é muito grande por favor digite um numero menor.")
    except ValueError as e:
        print("Valor inválido, por favor digite apenas numeros.")
    else:
        break

G = R * 180/3.14
print(f"O ângulo foi convertido para {G:.2f} graus.")
