"""
Exercicio 20: Dados três valores, A, B, C, verifique se eles podem ser valores dos lados de um triângulo e,
se forem, se é um triângulo escaleno, equilátero ou isóscele, considerando os seguintes conceitos:
- O comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados
- Chama-se equilátero o triângulo que tem três lados iguais.
- Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
- Recebe o nome de escaleno o triângulo que tem os três lados diferentes.
"""

print("Vamos ver se o triângulo é escaleno, equilátero ou isóscele")
TL1 = float(input("Digite o 1º lado do triângulo: "))
TL2 = float(input("Digite o 2º lado do triângulo: "))
TL3 = float(input("Digite o 3º lado do triângulo: "))

if TL1 < TL2 + TL3 and TL2 < TL1 + TL3 and TL3 < TL1 + TL2:
    if TL1 == TL2 and TL2 == TL3:
        print("É um triângulo equilátero.")
    elif TL1 == TL2 or TL2 == TL3 or TL1 == TL3:
        print("É um triângulo isósceles.")
    else:
        print("É um triângulo escaleno.")
else:
    print("Não é possivel formar um triângulo.")

