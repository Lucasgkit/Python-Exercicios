"""
Exercicio 28: Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos três valores lidos.
"""

print("Por favor digite três valores")
valor1 = float(input())
valor2 = float(input())
valor3 = float(input())
valor1Q = valor1 ** 2
valor2Q = valor2 ** 2
valor3Q = valor3 ** 2
resul = valor1Q + valor2Q + valor3Q

print(f"A soma do quadrado dos 3 valores é {resul:.2f}")
