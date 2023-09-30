"""
Exercicio 42: Receba o salário-base de um funcionário. Calcule e imprima o salário a receber,
sabendo-se que esse funcionário tem uma gratificação de 5% sobre o salário-base. Alem disso
ele paga 7% de imposto sobre o salário-base.
"""

print("Vamos calcular quanto sera seu salario liquido")
print("Por favor infome quanto é seu salario bruto")
while True:
    try:
        SB = float(input())
        if not -10000 <= SB <= 10000:
            raise ValueError("Este numero é muito grande por favor digite um numero menor.")
    except ValueError as e:
        print("Valor inválido, por favor digite apenas numeros.")
    else:
        break

IR = (SB/100) * 7
G = (SB/100) * 5
SL = SB - IR + G

print(f"Seu salario liquido fica R${SL:.2f}")
