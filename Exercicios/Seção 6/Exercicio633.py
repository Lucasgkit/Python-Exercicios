"""
Exercicio 33: Dados n e dois números inteiros positivos, i e j, diferentes de 0, imprimir em ordem
crescente os n primeiros naturais que são multiplos de i ou de j e ou de ambos.
Exemplo: Para n = 6, i = 2 e j = 3 a saida deverá ser: 0,2,3,4,6,8.
"""

n = int(input("Quantos valores quer ver: "))
i = int(input("Digite o valor do primeiro multiplo: "))
j = int(input("Digite o valor do segundo multiplo: "))

E = 0
N = 0

while E < n:
    if N % i == 0 or N % j == 0:
        if E > 0:
            print(",", end=" ")
        print(N, end="")
        E += 1
    N += 1

print()
