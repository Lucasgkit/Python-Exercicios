"""
Exercicio 3: Leia um número real. Se o número for positivio imprima a raiz quadrada.
Do contrário imprima o número ao quadrado.
"""

print("Por favor digite um número")
N = float(input())

if N > 0:
    R = N ** 0.5
    print(f"√{N:.2f} é {R:.2f}")
else:
    R = N ** 2
    print(f"{N}² é {R}")
