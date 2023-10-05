"""
Exercicio 39: Uma empresa decide dar um aumento aos seus funcionários de acordo com uma tabela que
considera o salário atual e o tempo de serviço de cada funcionário. Os funcionários com menor
salário terão um aumento proporcionalmente maior do que os funcionários com uma salário maior,
e conforme o tempo de serviço na empresa, cada funcionário irá receber um bônus adicional de
salário. Faça um programa que leia:
- O valor do salário atual do funcionário
- O tempo de serviço desse funcionário na empresa (número de anos de trabalho na empresa).

Use as tabelas abaixo para calcular o salário reajustado deste funcionário e imprima o valor
do salário final reajustado, ou uma mensagem caso o funcionário não tenha direito a nenhum aumento.

Salário atual       |   Reajuste    |   Tempo de Serviço    |   Bônus
até 500,00          |      25%      |    abaixo de 1 ano    | Sem bônus
até 1.000,00        |      20%      |     De 1 a 3 anos     |   100,00
até 1.500,00        |      15%      |     De 4 a 6 anos     |   200,00
até 2.000,00        |      10%      |     De 7 a 10 anos    |   300,00
acima de 2.000,00   | Sem reajuste  |    Mais de 10 anos    |   500,00
"""

print("Vamos calcular seu salário novo")
SA = float(input("Por favor digite seu salário atual: "))
TS = int(input("Quantos anos você trabalha na empresa? "))

if SA <= 500:
    SR = SA + (SA * 0.25)
elif SA <= 1000:
    SR = SA + (SA * 0.20)
elif SA <= 1500:
    SR = SA + (SA * 0.15)
elif SA <= 2000:
    SR = SA + (SA * 0.10)
else:
    SR = SA

if TS > 10:
    SN = SR + 500
elif 7 <= TS <= 10:
    SN = SR + 300
elif 4 <= TS <= 6:
    SN = SR + 200
elif 1 <= TS <= 3:
    SN = SR + 100
else:
    SN = SR

print(f"Seu novo salário é: R${SN:.2f}")
