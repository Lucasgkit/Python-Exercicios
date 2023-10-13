"""
Exercicio 22: escreva um programa completo que permita a qualquer aluno introduzir, pelo teclado,
uma sequência arbitraria de notas (válidas no intervalo de 10 a 20) e que mostre na tela, como
resultado, a correspondente média aritmética. O número de notas com que o aluno pretenda
efetuar o cálculo não será fornecido ao programa, o qual terminará quando for introduzido
um valor que não seja válido como nota de aprovação.
"""

T = 0
Q = 0

print("Para finalizar digite 0.")
while True:
    N = float(input("Digite uma nota (entre 10 a 20): "))

    if 10 <= N <= 20:
        T += N
        Q += 1
    else:
        if N == 0:
            M = T / Q
            print(f"A média aritmética é: {M:.2f}")
            break
        else:
            print("Nota invalida")


