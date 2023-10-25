"""
Exercicio 35: Faça um programa que some os números impares contidos em um intervalo definido
pelo usuário. O usuário define o valor incial do intervalo e o valor final deste intervalo
e o pgrama deve somar todos os números impares contidos neste intervalo. Caso o usuário
digite um intervalo inválido (começando por um valor maior que o valor final) deve ser
escrito uma mensagem de erro na tela, "Intervalo de valores inválido" e o programa termina.
Exemplo de tela de saida: Digite o valor inicial e valor final: 5 10
Soma dos impares neste intervalo: 21
"""

VI = int(input("Digite o valor inicial: "))
VF = int(input("Digite o valor final: "))

if VI > VF:
    print("Intervalo de valores inválido")
else:
    S = 0
    for N in range(VI, VF + 1):
        if N % 2 != 0:
            S += N
    print(f"Soma dos ímpares neste intervalo: {S}")
