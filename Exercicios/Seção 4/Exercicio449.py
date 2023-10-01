"""
Exercicio 49: Faça um programa para ler o horário (hora, minuto e segundo) de inicio e a duração,
em segundos de uma experiência biológica. O programa de ve resultar com o novo horário do termino da mesma.
"""

print("Digite o horario atual em segundos")
while True:
    try:
        HA = int(input())
        if not 0 <= HA <= 10000000000:
            raise ValueError("Número muito grande tente outro.")
    except ValueError as e:
        print("Valor inválido, por favor digite apenas numeros.")
    else:
        break

print("Digite tempo de duração em segundos")
while True:
    try:
        HD = int(input())
        if not 0 <= HD <= 10000000000:
            raise ValueError("Número muito grande tente outro.")
    except ValueError as e:
        print("Valor inválido, por favor digite apenas numeros.")
    else:
        break

#Horario atual
AH = HA // 3600
ARH = HA % 3600
AM = ARH // 60
AS = HA % 60

#Tempo Experiência
DH = HD // 3600
DRH = HD % 3600
DM = DRH // 60
DS = HD % 60

#Horario final
NH = HA + HD
H = NH // 3600
RH = NH % 3600
M = RH // 60
S = NH % 60

print(f"O horario atual é {AH}h {AM}m {AS}s")
print(f"O tempo da experiência é {DH}h {DM}m {DS}s")
print(f"O horario que acabará a experiência é {H}h {M}m {S}s")
