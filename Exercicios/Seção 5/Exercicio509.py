"""
Exercicio 9: Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a
prestração for maior que 20% do salário imprima: Empréstimo não concedido, caso contrário
imprima: Empréstimo concedido.
"""

print("Qual é o seu salário?")
S = float(input())
print("Qual o valor da prestação do empréstimo?")
E = float(input())

EL = (S/100) * 20

if E > EL:
    print("Empréstimo não concedido.")
else:
    print("Empréstimo concedido.")
