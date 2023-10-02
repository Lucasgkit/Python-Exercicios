"""
Exercicio 2: Leia um número fornecido pelo usuário. Se esse número for positivio, calcule a riz
quadrada do número. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.
"""

print("Por favor digite um número")
N = float(input())

if N > 0:
    R = N ** 0.5
    print(f"√{N:.2f} é {R:.2f}")
else:
    print("Número inválido")
