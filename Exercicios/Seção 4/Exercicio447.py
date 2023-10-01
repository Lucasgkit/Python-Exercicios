"""
Exercicio 47: Leia um número inteiro de 4 digitos de (1000 a 9999) e imprima 1 digito por linha.
"""

print("Digite um número inteiro de 1000 a 9999")
while True:
    try:
        NL = int(input())
        if not 1000 <= NL <= 9999:
            raise ValueError("Por favor respeite o padrão de 100 a 999")
    except ValueError as e:
        print("Valor inválido, por favor digite apenas numeros.")
    else:
        break

NG = str(NL)

print(NG[0])
print(NG[1])
print(NG[2])
print(NG[3])
