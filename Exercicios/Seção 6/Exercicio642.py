"""
Exercicio 42: Faça um programa que leia um conjunto não determinado de valores, um de cada vez, e
escreva para cada um dos valores lidos, o quadrado, o cubo e a raiz quadrada. Finalize a entrada
de dados com um valor negativo ou zero.
"""

while True:
    V = float(input("Digite um valor (negativo ou zero para encerrar): "))
    if V <= 0:
        break

    Q = V ** 2
    C = V ** 3
    R = V ** 0.5

    print(f"Valor: {V}")
    print(f"Quadrado: {Q}")
    print(f"Cubo: {C}")
    print(f"Raiz Quadrada: {R}\n")

print("Programa encerrado.")
