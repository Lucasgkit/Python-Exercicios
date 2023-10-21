"""
Exercicio 30: Faça um programa para calcular as seguintes sequências:
1 + 2 + 3 + 4 + 5 + ... + n
1 - 2 + 3 - 4 + 5 + ... + (2n - 1)
1 + 3 + 5 + 7 + ... + (2n - 1)
"""

n = int(input("Digite o valor de n: "))

S1 = sum(range(1, n + 1))

S2 = sum((-1) ** (i + 1) * i for i in range(1, 2 * n))

S3 = sum(range(1, 2 * n, 2))

print(f"A soma da sequência 1 + 2 + 3 + ... + {n} é: {S1}")
print(f"A soma da sequência 1 - 2 + 3 - 4 + ... + {2*n - 1} é: {S2}")
print(f"A soma da sequência 1 + 3 + 5 + 7 + ... + {2*n - 1} é: {S3}")

