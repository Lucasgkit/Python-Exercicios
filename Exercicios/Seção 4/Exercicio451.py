"""
Exercicio 51: Escreva um programa que leia as coordenadas X e Y de pontos no R² e calcule sua
distância da origem (0,0).
"""

print("Vamos calcular a distância por favor diga o X¹")
X1 = float(input())
print("Por favor diga o X²")
X2 = float(input())
print("Por favor diga o Y¹")
Y1 = float(input())
print("Por favor diga o Y²")
Y2 = float(input())

R = ((X1 - X2) ** 2 + (Y1 - Y2) ** 2) ** 0.5

print(f"A distância é {R:.2f}")