"""
Exercicio 20: Leia um valor de massa em quilogramas e apresente-o convertido em libras.
"""

print("Vamos fazer uma conversão de quilogramas para libras.")
print("Digite quantos quilogramas quer converter?")
while True:
    try:
        K = float(input())
        if not -10000 <= K <= 10000:
            raise ValueError("Este numero é muito grande por favor digite um numero menor.")
    except ValueError as e:
        print("Valor inválido, por favor digite apenas numeros.")
    else:
        break

L = K / 0.45
print(f"A conversão resultou em {L:.2f} libras.")
