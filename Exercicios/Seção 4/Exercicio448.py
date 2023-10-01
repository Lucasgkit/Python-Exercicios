"""
Exercicio 48: Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos.
"""

print("Digite um número inteiro para ser convertida em horario")
while True:
    try:
        NI = int(input())
        if not 0 <= NI <= 10000000000:
            raise ValueError("Número muito grande tente outro.")
    except ValueError as e:
        print("Valor inválido, por favor digite apenas numeros.")
    else:
        break

H = NI // 3600
RH = NI % 3600
M = RH // 60
S = RH % 60

print(f"{H}h {M}m {S}s")
