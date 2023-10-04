"""
Exercicio 26: Leia a distância em Km e a quantidade de litros de gasolina consumidos por um carro
em um percuso, calcule o consumo em KM/L e escreva uma mensagem de acordo com a tabela abaixo:
Consumo     |  Km/l  | mensagem
menor que   |    8   | Venda o carro!
entre       | 8 e 14 | Econômico!
maior que   |   12   | Super econômicoo!
"""

print("Vamos calcular o consumo do seu carro")
Km = float(input("Quantos Km percorreu? "))
L = float(input("Quantos Litros consumiu? "))
R = Km/L
if R < 8:
    print("Venda o carro!")
elif 8 <= R < 14:
    print("Econômico!")
else:
    print("Super econômicoo!")
