"""
Exercicio 38: Leia o salário de um funcionário. calcule e imprima o valor do novo salário,
sabendo que ele recebeu um aumento de 25%
"""

print("Por favor digite o valor do seu salario")
while True:
    try:
        S = float(input())
        if not -10000 <= S <= 10000:
            raise ValueError("Este numero é muito grande por favor digite um numero menor.")
    except ValueError as e:
        print("Valor inválido, por favor digite apenas numeros.")
    else:
        break

A = (S/100) * 25
resul = S + A
print(f"O seu novo salario é de {resul:.2f}")
