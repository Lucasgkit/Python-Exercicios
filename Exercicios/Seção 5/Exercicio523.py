"""
Exercicio 23: Determine se um determinado ano lido é bissexto. Sendo que um ano é bissexto se
for divisivel por 400 ou se for divisivel por 4 e não for divisivel por 100.
Por exemplo: 1988, 1992, 1996
"""

print("Verificador de ano Bissexto")
ano = int(input("Qual ano quer verificar? "))

if ano % 4 == 0 and ano % 100 != 0:
    print("O ano é bissexto")
else:
    print("O ano não é bissexto")
