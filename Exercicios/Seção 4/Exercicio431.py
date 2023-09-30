"""
Exercicio 30: Leia um valor em real e a cotação do dólar.
Em seguida, imprima o valor correspondente em dólares
"""

print("Vamos fazer a conversão de reais para dólares")
print("Por favor digite quantos reais quer converter")
R = float(input())
print("Por favor digite a cotação do dólar")
C = float(input())

D = R * C

print(f"A conversão deu ${D:.2f} dólares")
