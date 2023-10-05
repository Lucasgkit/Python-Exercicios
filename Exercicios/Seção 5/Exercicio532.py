"""
Exercicio 32: Escreva um programa que leia o código do produto escolhido do cardápio de uma lanchonete
e a quantidade. O programa deve calcular o valor a ser pago por aquele lanche.
Considere que a cada execução somente será calculado um pedido. O cardápio da lanchonete segue o padrão abaixo:
Especificações      |   Código   |  Preço
Cachorro Quente     |    100     |  1,20
Bauru Simples       |    101     |  1,30
Bauru com Ovo       |    102     |  1,50
Hamburguer          |    103     |  1,20
Cheeseburguer       |    104     |  1,70
Suco                |    105     |  2,20
Refrigerante        |    106     |  1,00
"""

print("Segue nosso cardápio: ")
print("Especificações      |   Código   |  Preço")
print("Cachorro Quente     |    100     |  1,20")
print("Bauru Simples       |    101     |  1,30")
print("Bauru com Ovo       |    102     |  1,50")
print("Hamburguer          |    103     |  1,20")
print("Cheeseburguer       |    104     |  1,70")
print("Suco                |    105     |  2,20")
print("Refrigerante        |    106     |  1,00")

Pedido = int(input("Digite o código do produto desejado: "))
Quantidade = int(input("Quantos vai querer? "))

if Pedido == 100:
    Preço = Quantidade * 1.20
    print(f"Total: R${Preço:.2f}")
elif Pedido == 101:
    Preço = Quantidade * 1.30
    print(f"Total: R${Preço:.2f}")
elif Pedido == 102:
    Preço = Quantidade * 1.50
    print(f"Total: R${Preço:.2f}")
elif Pedido == 103:
    Preço = Quantidade * 1.20
    print(f"Total: R${Preço:.2f}")
elif Pedido == 104:
    Preço = Quantidade * 1.70
    print(f"Total: R${Preço:.2f}")
elif Pedido == 105:
    Preço = Quantidade * 2.20
    print(f"Total: R${Preço:.2f}")
elif Pedido == 106:
    Preço = Quantidade * 1.00
    print(f"Total: R${Preço:.2f}")
else:
    print("O código não existe")

