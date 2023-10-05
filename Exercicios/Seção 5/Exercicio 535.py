"""
Exercicio 35: Leia uma data e determine se ela é válida. Ou seja, verifique se o mês está entre 1 e 12,
e se o dia existe naquele mês. Note que Fevereiro tem 29 dias em anos bissextos, e 28 em
dias em ano não bissextos.
"""

print("Verificador de dia válido.")
Dia = int(input("Que dia quer verificar? "))
Mes = int(input("De qual mes? "))
Ano = int(input("De qual ano? "))

bissexto = (Ano % 4 == 0 and Ano % 100 != 0) or Ano % 400 == 0

if 1 <= Mes <= 12:
    if (Mes == 1 or Mes == 3 or Mes == 5 or Mes == 7 or Mes == 8 or Mes == 10 or Mes == 12) and 1 <= Dia <= 31:
        print("Dia válido")
    elif (Mes == 4 or Mes == 6 or Mes == 9 or Mes == 11) and 1 <= Dia <= 30:
        print("Dia válido")
    elif Mes == 2:
        if bissexto and 1 <= Dia <= 29:
            print("Dia válido")
        elif not bissexto and 1 <= Dia <= 28:
            print("Dia válido")
        else:
            print("Dia inválido")
    else:
        print("Dia inválido")
else:
    print("Mês inválido")
