"""
Exercicio 25: Calcule as raizes da equação de 2º grau.
lembrando que: x=(-b +- √b² - 4ac)/2 e ax² + bx + c = 0 representa uma equação de 2º grau.
a variável a tem que ser diferente de zero. Caso seja igual, imprima a mensagem "não é equação de segundo grau".
- Se delta < 0 não existe real, IMprima a mensagem Não existe raiz.
- Se delta = 0 existe uma raiz real, imprima a raiz e a mensagem Raiz unica
- Se delta >= 0 imprima as duas raizes reais
"""

print("Vamos calcular as raizes da equação de 2º grau")
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

if a == 0:
    print("Não é equação de 2º grau")
else:
    delta = b ** 2 - 4 * a * c

    if delta < 0:
        print("Não existe raiz.")
    elif delta == 0:
        R = -b / (2 * a)
        print(f"Raiz unica: {R}")
    else:
        R1 = (-b + (delta ** 0.5)) / (2 * a)
        R2 = (-b - (delta ** 0.5)) / (2 * a)
        print(f"Raiz 1: {R1}")
        print(f"Raiz 2: {R2}")
