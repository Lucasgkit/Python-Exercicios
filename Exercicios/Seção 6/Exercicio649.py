"""
Exercicio 49: O funcionário chamado Carlos tem um colega chamado João que recebe um salário que
equivale a um terço do seu salário. Carlos gosta de fazer aplicações na caderneta de poupança
e vai aplicar seu salário integralmente nela, pois estpa rendendo 2% ao mês. João aplicará seu
salário integralmente no fundo de renda fixa, que está rendendo 5% ao Mês. Construa um programa
que deverá calcular e mostrar a quantidade de meses necessários para que o valor pertencente a
João iguale ou ultrapasse o valor pertencente a Carlos. Teste com outros valores para as taxas.
"""

SC = float(input("Digite o salário de Carlos: "))
SJ = SC / 3
TP = 0.02
TR = 0.05

M = 0

while SJ < SC:
    SC += SC * TP
    SJ += SJ * TR
    M += 1

print(f"Em {M} meses, o valor pertencente a João igualará ou ultrapassará o valor pertencente a Carlos.")
