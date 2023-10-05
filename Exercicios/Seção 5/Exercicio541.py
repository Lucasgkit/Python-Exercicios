"""
Exercicio 41: Faça um algoritmo que calcule o IMC de uma pessoa e mostre sua classificação de
acordo com a tabela abaixo:

    IMC     |   Classificação
  < 18.5    |   Abaixo do peso
18,6 - 24,9 |   Saudável
25,0 - 29,9 |   Peso em excesso
30,0 - 34,9 |   Obesidade Grau I
35,0 - 39,9 |   Obesidade Grau II (severa)
   >= 40    |   Obesidade Grau III (mórbida)
"""

print("Vamos calcular o seu IMC")
A = float(input("Qual sua altura? "))
P = float(input("Qual seu peso? "))
IMC = P / (A ** 2)

if IMC < 18.5:
    print(f"Seu IMC é {IMC:.1f} e você se encontra abaixo do peso")
elif 18.6 <= IMC <= 24.9:
    print(f"Seu IMC é {IMC:.1f} e você se encontra com o peso saudável")
elif 25 <= IMC <= 29.9:
    print(f"Seu IMC é {IMC:.1f} e você se encontra com peso em excesso")
elif 30 <= IMC <= 34.9:
    print(f"Seu IMC é {IMC:.1f} e você se encontra com obesidade grau I")
elif 35 <= IMC <= 39.9:
    print(f"Seu IMC é {IMC:.1f} e você se encontra com obesidade grau II")
else:
    print(f"Seu IMC é {IMC:.1f} e você se encontra com oobesidade grau III")