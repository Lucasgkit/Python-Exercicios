"""
Exercicio 4: Faça um programa que leia um número e, caso seja positivio, calcule e mostre:
- O número digitado ao quadrado
- A raiz quadrada do número digitado
"""

print("Por favor digite um número")
N = float(input())

if N > 0:
    R = N ** 0.5
    R2 = N ** 2
    print(f"√{N:.2f} é {R:.2f}")
    print(f"{N}² é {R2}")
else:
    print("Número inválido")
