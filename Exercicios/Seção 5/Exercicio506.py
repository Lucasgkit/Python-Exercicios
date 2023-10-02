"""
Exercicio 6: Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles,
assim como a diferença existente entre ambos
"""

print("Digite um número inteiro")
N1 = int(input())
print("Digite outro número inteiro")
N2 = int(input())

if N2 < N1:
    print(f"{N1} é maior que {N2}")
    R = N1 - N2
    print(f"{R} é a diferença entre eles")
elif N2 == N1:
    print(f"Ambos tem o mesmo valor")
else:
    print(f"{N2} é maior que {N1}")
    R = N2 - N1
    print(f"{R} é a diferença entre eles")
