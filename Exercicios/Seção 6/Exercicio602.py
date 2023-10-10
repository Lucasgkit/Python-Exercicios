"""
Exercicio 2: Escreva um programa que escreva na tela, de 1 até 100, de 1 em 1, 3 vezes. A primeira
vez deve usar a estrutura de repetição for, a segunda while, e a terceira do while.
"""

print("Usando a estrutura for:")

for i in range(1, 101):
    print(i)
print("\n")

print("Usando a estrutura while")

N = 0
while N < 100:
    N += 1
    print(N)

print("Usando a estrutura do while")

N = 0
while True:
    N += 1
    print(N)
    if N == 100:
        break
