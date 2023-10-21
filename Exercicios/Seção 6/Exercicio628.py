"""
Exercicio 28: Faça um programa que leia um valor N inteiro e positivo, calcule e mostre o valor E,
conforme a fórmula a seguir:
E = 1 + 1/1! + 1/2! + 1/3! + ... + 1/N!
"""

n = int(input("Digite um valor inteiro e positivo N: "))

if n < 0:
    print("Por favor, digite um número inteiro e positivo.")
else:
    e = 1.0
    f = 1

    for i in range(1, n + 1):
        f *= i
        e += 1 / f  

    print(f"O valor de E é: {e:.10f}")
