"""
Exercicio 46: Faça um programa que leia um número inteiro positivio de tres digitos (de 100 a 999).
Gere outro número formado pelos digitos invertido do número lido. Exemplo:
Número lido ->   123
Número gerado -> 321
"""

print("Digite um número inteiro de 100 a 999")
while True:
    try:
        NL = int(input())
        if not 100 <= NL <= 999:
            raise ValueError("Por favor respeite o padrão de 100 a 999")
    except ValueError as e:
        print("Valor inválido, por favor digite apenas numeros.")
    else:
        break

NG = str(NL)

print(f"Devolvendo o numero invertido: {NG[::-1]}")
