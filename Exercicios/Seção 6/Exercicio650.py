"""
Exercicio 50: Chico tem 1,50 metros e cresce 2 centímetros por ano, enquanto Zé tem 1,10 metros e
cresce 3 centímetros por ano. Escreva um programa que calcule e imprima quantos anos serão
necessários para que Zé seja maior que Chico.
"""

AC = 150
AZ = 110
CC = 2
CZ = 3
A = 0

while AZ <= AC:
    AC += CC
    AZ += CZ
    A += 1

print(f"Serão necessários {A} anos para que Zé seja mais alto que Chico.")
