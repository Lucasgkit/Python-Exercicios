"""
Exercicio 32: Leia um número inteiro e imprima a soma do sucessor de seu triplo com
o antecessor de seu dobro.
"""

print("Por favor digite um número inteiro")
num = int(input())
nums = (num ** 3) + 1
numa = (num ** 2) - 1
resul = nums + numa
print(f"A soma do sucessor de seu triplo com o antecessor de seu dobre é {resul}")
