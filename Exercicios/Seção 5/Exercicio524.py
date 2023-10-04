"""
Exercicio 24: Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado
possui uma taxa diferente de imposto sobre o produto (MG 7%; SP 12%; RJ 15%; MS 8%).
Faça um programa em que o usuário entre com o valor e o estado destino do produto e o
programa retorne o preço final do produto acrescido do imposto do estado em que ele será
vendido. Se o estado digitado não for válido, mostrar uma mensagem de erro.
"""

valor = float(input("Qual o valor do produto? "))
estado = input("Digite a sigla do seu estado: ").upper()

if estado == "MG":
    R = valor + (valor/100 * 7)
    print(f"Total: {R}")
elif estado == "SP":
    R = valor + (valor/100 * 12)
    print(f"Total: {R}")
elif estado == "RJ":
    R = valor + (valor/100 * 15)
    print(f"Total: {R}")
elif estado == "MS":
    R = valor + (valor/100 * 8)
    print(f"Total: {R}")
else:
    print("Ainda não trabalhamos com o seu estado.")