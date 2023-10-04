"""
Exercicio 21: Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação escolhida.
Escreva uma mensagem de erro se a opção foir inválida.

Escolha a opção:
1- Soma de 2 núemros.
2- Diferença entre 2 números (maior pelo menor)
3- Produto entre 2 números.
4- Divisão entre 2 números (o denominador não pode ser zero).
"""

print("Escolha a opção:")
print("1- Soma de 2 núemros.")
print("2- Diferença entre 2 números (maior pelo menor)")
print("3- Produto entre 2 números.")
print("4- Divisão entre 2 números (o denominador não pode ser zero).")
E = int(input("Digite a opção desejada: "))
if E < 1 or E > 4:
    print("Opção invalida")
    exit()
else:
    V1 = float(input("Digite o 1º valor: "))
    V2 = float(input("Digite o 2º valor: "))

    if E == 1:
        R = V1 + V2
        print(f"Resultado: {R}")
    if E == 2:
        if V1 > V2:
            R = V1 - V2
            print(f"Resultado: {R}")
        else:
            R = V2 - V1
            print(f"Resultado: {R}")
    if E == 3:
        R = V1 * V2
        print(f"Resultado: {R}")
    if E == 4:
        if V2 == 0:
            print("Não é possivel dividir por zero.")
        else:
            R = V1 / V2
            print(f"O resultado é {R}")
