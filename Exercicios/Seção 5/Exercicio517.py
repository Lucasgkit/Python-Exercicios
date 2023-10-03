"""
Exercicio 17: Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que:
A = ((basemaior + basemenor) * altura) / 2
Lembre-se a base maior e a base menor devem ser números maiores que zero
"""

print("Vamos calcular a área de um trapézio")
BMA = float(input("Digite o valor da base maior: "))
BME = float(input("Digite o valor da base menor: "))
A = float(input("Digite o valor da altura: "))
if BMA <= 0 or BME <= 0:
    print("As bases não podem ser menor que 0")
else:
    R = ((BMA + BME) * A) / 2
    print(f"A área do trapézio é {R}")
