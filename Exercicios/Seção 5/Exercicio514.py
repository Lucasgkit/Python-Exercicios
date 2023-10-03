"""
Exercicio 14: A nota final de um estudante é calculada a partir de três notas atribuidas entre o intervalo
de 0 até 10, respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame final.
A média das três notas menciondas anteriormente obedece aos pesos:
Trabalho de Laboratorio:  2
Avaliação Semestral:      3
Exame final:              5
De acordo com o resultado, mostre na tela se o aluno esta:
Reprovado:                0 a 2.9
Recuperação:              3 a 4.9
Aprovado:                 5 a 10
"""

print("Vamos calcular a sua media")
print("Qual a nota do trabalho de laboratorio?")
N1 = float(input())
print("Qual a nota da avaliação semestral?")
N2 = float(input())
print("Qual a nota do exame final?")
N3 = float(input())

P1 = N1 * 2
P2 = N2 * 3
P3 = N3 * 5
R = (P1 + P2 + P3) / 10

print(f"Sua media é {R}")

if R < 3:
    print("Reprovado")
elif R < 5:
    print("Recuperação")
else:
    print("Aprovado")
