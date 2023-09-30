"""
Exercicio 39: A importância de R$ 780.000,00 será dividida entre três ganhadores de um concurso.
Sendo que da quantia total:
1º ganhador receberá 46%
2º ganhador receberá 32%
3º ganhador receberá o restante
Calcule e impra a quantia ganha por cada um dos ganhadores
"""

print("Vamos anunciar quanto cada ganhador receberá de nosso premio")
P = 780000.00

G1 = (P/100) * 46
G2 = (P/100) * 32
G3 = P - G1 - G2

print(f"O ganhador em 1º lugar ganhou R${G1:.2f}")
print(f"O ganhador em 2º lugar ganhou R${G2:.2f}")
print(f"O ganhador em 3º lugar ganhou R${G3:.2f}")