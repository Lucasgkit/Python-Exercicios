"""
Exercicio 21: Leia um valor de massa em libras e apresente-o convertido em quilogramas.
"""

print("Vamos fazer uma conversão de libras para quilogramas.")
print("Digite quantas libras quer converter?")
while True:
    try:
        L = float(input())
        if not -10000 <= L <= 10000:
            raise ValueError("Este numero é muito grande por favor digite um numero menor.")
    except ValueError as e:
        print("Valor inválido, por favor digite apenas numeros.")
    else:
        break

K = L * 0.45
print(f"A conversão resultou em {K:.2f} quilogramas.")
