"""
Exercicio 38: Faça um programa que calcule o terno pitagórico a, b, c, para o qual a + b + c = 1000.
Um terno pitagórico é um conjunto de três números naturais, a, b, c, para a qual,
Por exemplo: a² + b² = c²
            3² + 4² = 9 + 16 = 25 = 5²
"""

for a in range(1, 1000):
    for b in range(a, 1000 - a):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print(f"O terno pitagórico é a = {a}, b = {b}, c = {c}")
            break
