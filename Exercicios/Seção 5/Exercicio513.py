"""
Exercicio 13: Faça um algoritmo que calcule a média ponderada das notas de 3 provas.
A primeira e a segunda prova tem peso 1 e a terceira tem peso 2. AO final mostrar
a média do aluno e indicar se o aluno foi aprovado ou reprovado. A nota para
aprovação deve ser igual ou superior a 60 pontos.
"""

print("Vamos calcular a sua media")
print("Qual a nota da 1º prova?")
N1 = float(input())
print("Qual a nota da 2º prova?")
N2 = float(input())
print("Qual a nota da 3º prova?")
N3 = float(input())

P1 = N1 * 1
P2 = N2 * 1
P3 = N3 * 2
R = (P1 + P2 + P3) / 4

print(f"Sua media é {R}")

if R > 60:
    print("Você foi aprovado")
else:
    print("Você foi reprovado")
