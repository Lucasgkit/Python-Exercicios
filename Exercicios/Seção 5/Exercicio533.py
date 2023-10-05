"""
Exercicio 33: Um produto vai sofrer aumento de acordo com a tabela abaixo. Leia o preço antigo,
calcule e escreba o preço novo, e escreva uma mensagem em função do preço novo (de acordo com
a segunda tabela).
Preço antigo        |   Percentual de aumento
até R$50            |           5%
entre R$50 e R$100  |           10%
acima de R$100      |           15%

Preço novo          |   Mensagem
até R%80            |   Barato
entre R$80 a R$120  |   Normal
entre R$120 e R$200 |   Caro
acima de R$200      |   Muito caro
"""

print("Vamos calcular o novo preço")
PA = float(input("Qual o valor do preço antigo que deseja calcular? "))

if PA <= 50:
    PN = PA + (PA * 0.05)
elif 50 < PA <= 100:
    PN = PA + (PA * 0.10)
else:
    PN = PA + (PA * 0.15)

if PN <= 80:
    print(f"Valor novo: R${PN:.2f}. o preço está barato.")
elif 80 < PN <= 120:
    print(f"Valor novo: R${PN:.2f}. o preço está normal.")
elif 120 < PN <= 200:
    print(f"Valor novo: R${PN:.2f}. o preço está caro.")
else:
    print(f"Valor novo: R${PN:.2f}. o preço stá muito caro.")
