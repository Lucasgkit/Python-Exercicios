"""
Exercicio 16: Leia um valor de comprimento em polegadas e apresente-o convertido em centimetros.
"""

print("Vamos fazer uma conversão de polegadas para centimetros.")
print("Digite quantas polegadas quer converter?")
while True:
    try:
        P = float(input())
        if not -10000 <= P <= 10000:
            raise ValueError("Este numero é muito grande por favor digite um numero menor.")
    except ValueError as e:
        print("Valor inválido, por favor digite apenas numeros.")
    else:
        break

C = P * 2.54
print(f"O comprimento convertido é de {C:.2f}cm.")
