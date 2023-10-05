"""
Exercicio 38: Leia uma data de nascimento de uma pessoa fornecida através de três números inteiros:
Dia, Mes e Ano. Teste a validade desta data para saber se esta é uma data válida. Teste se o dia
fornecido é um dia válido: dia > 0, dia <= 28 para o mes de fevereiro (29 se o ano for bissexto),
dia <= 30 em abril, junho, setembro e novembro, dia <= 31 nos outros meses. Teste a validade do
mes: mes > 0 e mes < 13. Teste a validade do ano: ano < ano atual (use uma constante definida
com o valor igual a 2008) Imprimir: "data válida" ou "data inválida" no final da execução do programa.
"""

print("Verificador de data válida.")
Dia = int(input("Por favor informe o dia: "))
Mes = int(input("Por favor informe o mes: "))
Ano = int(input("Por favor informe o ano: "))
AnoAtual = 2008

bissexto = (Ano % 4 == 0 and Ano % 100 != 0) or Ano % 400 == 0

if Ano <= AnoAtual:
    if 0 < Mes <= 12:
        if (Mes == 4 or Mes == 6 or Mes == 9 or Mes == 11) and 0 < Dia <= 30:
            print("Data válida")
        elif (Mes == 1 or Mes == 3 or Mes == 5 or Mes == 7 or Mes == 8 or Mes == 10 or Mes == 12) and 0 < Dia <= 31:
            print("Data válida")
        elif Mes == 2:
            if bissexto and 1 <= Dia <= 29:
                print("Dia válido")
            elif not bissexto and 1 <= Dia <= 28:
                print("Dia válido")
            else:
                print("Dia inválido")
        else:
            print("Data inválida")
    else:
        print("Data inválida")
else:
    print("Data inválida")
