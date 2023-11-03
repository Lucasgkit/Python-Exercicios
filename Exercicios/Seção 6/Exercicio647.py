"""
Exercicio 47: Faça um programa que apresente um mneu de opções para o cálculo das seguintes operações
entre dois números:
- adição (opção 1)
- subtração (opção 2)
- multiplicação (opção 3)
- divisão (opção 4)
- saida ( opção 5)
O programa deve possibilitar ao usuário a escolha da operação desejada, a exibição do resultado e a
volta ao menu de opções. O programa só termina quando for escolhida a opção de saida (opção 5).
"""

while True:
    print("Escolha a operação desejada:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    O = input("Digite o número da opção desejada: ")

    if O == "5":
        print("Programa encerrado.")
        break

    if O in ("1", "2", "3", "4"):
        N1 = float(input("Digite o primeiro número: "))
        N2 = float(input("Digite o segundo número: "))

        if O == "1":
            R = N1 + N2
            print(f"A soma de {N1} e {N2} é igual a {R}")
        elif O == "2":
            R = N1 - N2
            print(f"A subtração de {N1} e {N2} é igual a {R}")
        elif O == "3":
            R = N1 * N2
            print(f"A multiplicação de {N1} e {N2} é igual a {R}")
        elif O == "4":
            if N2 == 0:
                print("Erro: divisão por zero.")
            else:
                R = N1 / N2
                print(f"A divisão de {N1} por {N2} é igual a {R}")
    else:
        print("Opção inválida. Por favor, escolha uma opção de 1 a 5.")
