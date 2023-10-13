"""
Exercicio 21: Faça um programa que receba dois números. Calcule e mostre:
- A soma dos números pares desse intervalo de números, incluindo os números digitados
- A multiplicação dos números impares desse intervalo, incluindo os digitados
"""

N1 = int(input("Digite o primeiro número: "))
N2 = int(input("Digite o segundo número: "))

SP = 0
MI = 1

if N1 > N2:
    N1, N2 = N2, N1

for N in range(N1, N2 + 1):
    if N % 2 == 0:
        SP += N
    else:
        MI *= N

print(f"Soma dos números pares: {SP}")
print(f"Multiplicação dos números ímpares: {MI}")

