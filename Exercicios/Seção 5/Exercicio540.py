"""
Exercicio 40: O custo ao consumidor de um carro novo é a soma do custo de fábrica, da comissão
do distribuidor, e dos impostos. A comissão e os impostos são calculados sobre o custo de fábrica,
de acordo com a tabela abaixo. Leia o custo de fábrica e escreva o custo do consumidor.

Custo de fábrica                |   % do distribuidor   |   % dos impstos
até R$12.000,00                 |           5           |      isento
entre R$12.000,00 e R$25.000,00 |           10          |        15
acima de R$25.000,00            |           15          |        20
"""

print("Vamos calcular o custo do consumidor")
CF = float(input("Qual o custo de fábrica? "))

if CF <= 12000:
    CD = CF * 0.05
    CI = CF * 0
elif 12000 < CF <= 25000:
    CD = CF * 0.10
    CI = CF * 0.15
else:
    CD = CF * 0.15
    CI = CF * 0.20

CC = CF + CD + CI
print(f"O custo para o consumidor é de: R${CC:.2f}")
