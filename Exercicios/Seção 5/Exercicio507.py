"""
Exercicio 7: Faça um programa que receba dois números e mostre o maior. Se por acaso, os dois
números forem iguais, imprima a mensagem números iguais.
"""

print("Digite um número")
N1 = input()
print("Digite outro número")
N2 = input()

if N2 == N1:
    print(f"São iguais")
else:
    print(f"Não são iguais")
