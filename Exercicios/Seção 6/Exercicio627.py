"""
Exercicio 27: Em Matemática, o número harmônico designado por H(n) define-se como sendo a soma
da série harmónica:
H(n) = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n
Faça um programa que leia um valor n inteiro e positivo e apresente o valor de H(n).
"""

n = int(input("Digite um valor inteiro e positivo n: "))

if n <= 0:
    print("Por favor, digite um número inteiro e positivo.")
else:
    hn = 0
    for i in range(1, n + 1):
        hn += 1 / i
    print(f"O valor de H({n}) é: {hn:.2f}")
