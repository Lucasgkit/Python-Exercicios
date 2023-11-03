"""
Exercicio 44: Leia um número positivo do usuário, então, calcule e imprima a sequência Fibonacci até
o primeiro número superior ao número lido. Exemplo: se o usuário informou o número 30, a sequência
a ser impressa será 0 1 1 2 3 5 8 13 21 34.
"""

N = int(input("Digite um número positivo: "))

if N <= 0:
    print("Por favor, forneça um número positivo.")
else:
    a, b = 0, 1
    while a <= N:
        if a > 0:
            print(a, end=' ')
        a, b = b, a + b
    print(a)
