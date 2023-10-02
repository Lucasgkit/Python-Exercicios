"""
Exercicio 1: Faça um programa que receba dois números e mostre qual deles é o maior.
"""

print("Digite um número")
N1 = input()
print("Digite outro número")
N2 = input()

if N2 < N1:
    print(f"{N1} é maior que {N2}")
elif N2 == N1:
    print(f"Ambos tem o mesmo valor")
else:
    print(f"{N2} é maior que {N1}")
