"""
Exercicio 36: Escreva um programa que, dado o valor da venda, imprima a comissão que deverá ser
paga ao vendedor. Para calcular a comissão, considere a tabela abaixo:

                    Venda mensal                        |           Comissão
Maior ou igual a R$100.000,00                           |   R$700,00 + 16% das vendas
Menor que R$100.000,00 e maior ou igual a R$80.000,00   |   R$650,00 + 14% das vendas
Menor que R$80.000,00 e maior ou igual a R$60.000,00    |   R$600,00 + 14% das vendas
Menor que R$60.000,00 e maior ou igual a R$40.000,00    |   R$550,00 + 14% das vendas
Menor que R$40.000,00 e maior ou igual a R$20.000,00    |   R$500,00 + 14% das vendas
Menor que R$20.000,00                                   |   R$400,00 + 14% das vendas
"""

print("Vamos calcular sua comissão")
Venda = float(input("Quanto foi o valor da venda? "))

if Venda >= 100000:
    C = 700 + (Venda * 0.16)
    print(f"Sua comissão é de R${C:.2f}")
elif 100000 > Venda >= 80000:
    C = 650 + (Venda * 0.14)
    print(f"Sua comissão é de R${C:.2f}")
elif 80000 > Venda >= 60000:
    C = 600 + (Venda * 0.14)
    print(f"Sua comissão é de R${C:.2f}")
elif 60000 > Venda >= 40000:
    C = 550 + (Venda * 0.14)
    print(f"Sua comissão é de R${C:.2f}")
elif 40000 > Venda >= 20000:
    C = 500 + (Venda * 0.14)
    print(f"Sua comissão é de R${C:.2f}")
elif 20000 > Venda:
    C = 400 + (Venda * 0.14)
    print(f"Sua comissão é de R${C:.2f}")