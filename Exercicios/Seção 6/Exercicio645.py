"""
Exercicio 45: Faça um algoritmo que converta uma velocidade expressa em km/h para m/s e vice
versa. Você deve criar um menu com as duas opções de conversão e com uma opção para finalizar
o programa. O usuário poderá fazer quantas conversões deseja, sendo que o programa só sera
finalizado quando a opção de finalizar fo escolhida.
"""

while True:
    print("Escolha uma opção:")
    print("1. Converter de km/h para m/s")
    print("2. Converter de m/s para km/h")
    print("3. Finalizar o programa")

    O = input("Digite o número da opção desejada: ")

    if O == "1":
        KMH = float(input("Digite a velocidade em km/h: "))
        MS = KMH * 1000 / 3600
        print(f"{KMH} km/h é igual a {MS} m/s")
    elif O == "2":
        MS = float(input("Digite a velocidade em m/s: "))
        KMH = MS * 3600 / 1000
        print(f"{MS} m/s é igual a {KMH} km/h")
    elif O == "3":
        print("Programa finalizado.")
        break
    else:
        print("Opção inválida. Por favor, escolha 1, 2 ou 3.")
