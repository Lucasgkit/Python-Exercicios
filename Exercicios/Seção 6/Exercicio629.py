"""
Exercicio 29: Escreva um programa para calcular o valor da série, para 5 termos.
S = 0 + 1/2! + 2/4! + 3/6! + ...
"""

S = 0
f = 1

for n in range(5):
    S += n / f
    n += 1  
    f *= (2 * n) * (2 * n + 1)

print(f"O valor da série para 5 termos é: {S:.6f}")
