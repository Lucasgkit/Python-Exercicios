"""
Exercicio 17: Leia um valor de comprimento em centimetros e apresente-o convertido em polegadas.
"""

print("Vamos fazer uma conversão de polegadas para centimetros.")
print("Digite quantas polegadas quer converter?")
while True:
    try:
        C = float(input())
        if not -10000 <= C <= 10000:
            raise ValueError("Este numero é muito grande por favor digite um numero menor.")
    except ValueError as e:
        print("Valor inválido, por favor digite apenas numeros.")
    else:
        break

P = C / 2.54
print(f"O comprimento convertido é de {P:.2f} polegadas.")
