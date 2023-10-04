"""
Exercicio 30: Faça um programa que receba três números e mostre-os em ordem crescente.
"""

print("Digite três números")
N1 = float(input())
N2 = float(input())
N3 = float(input())

menor_numero = N1
if N2 < menor_numero:
    menor_numero = N2
if N3 < menor_numero:
    menor_numero = N3

maior_numero = N1
if N2 > maior_numero:
    maior_numero = N2
if N3 > maior_numero:
    maior_numero = N3

if N1 != menor_numero and N1 != maior_numero:
    numero_medio = N1
if N2 != menor_numero and N2 != maior_numero:
    numero_medio = N2
if N3 != menor_numero and N3 != maior_numero:
    numero_medio = N3

print(f"Números em ordem crescente: {menor_numero}, {numero_medio}, {maior_numero}")
