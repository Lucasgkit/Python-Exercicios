"""
Exercicio 29: Faça uma prova de matemática para crianças que estão aprendendo a somar números
inteiros menores do que 100. Escolha números aleatórios entre 1 e 100, e mostre na tela a pergunta:
qual é a soma de a + b, onde a e b são os números aleatórios. Peça a resposta.
Faça cinco perguntas ao aluno, e mostre para ele as perguntas e as respostas corretas, além
de quantas vezes o aluno acertou.
"""
import random

a1 = random.randrange(1,100)
b1 = random.randrange(1,100)
a2 = random.randrange(1,100)
b2 = random.randrange(1,100)
a3 = random.randrange(1,100)
b3 = random.randrange(1,100)
a4 = random.randrange(1,100)
b4 = random.randrange(1,100)
a5 = random.randrange(1,100)
b5 = random.randrange(1,100)

print(f"1º Pergunta: Quanto é {a1} + {b1}?")
R1 = int(input())
print(f"2º Pergunta: Quanto é {a2} + {b2}?")
R2 = int(input())
print(f"3º Pergunta: Quanto é {a3} + {b3}?")
R3 = int(input())
print(f"4º Pergunta: Quanto é {a4} + {b4}?")
R4 = int(input())
print(f"5º Pergunta: Quanto é {a5} + {b5}?")
R5 = int(input())

RC = 0

if R1 == a1 + b1:
    print("Acertou a 1º pergunta")
    RC += 1
else:
    print(f"Errou a 1º pergunta, a resposta correta era {a1 + b1}")

if R2 == a2 + b2:
    print("Acertou a 2º pergunta")
    RC += 1
else:
    print(f"Errou a 2º pergunta, a resposta correta era {a2 + b2}")

if R3 == a3 + b3:
    print("Acertou a 3º pergunta")
    RC += 1
else:
    print(f"Errou a 3º pergunta, a resposta correta era {a3 + b3}")

if R4 == a4 + b4:
    print("Acertou a 4º pergunta")
    RC += 1
else:
    print(f"Errou a 4º pergunta, a resposta correta era {a4 + b4}")

if R5 == a5 + b5:
    print("Acertou a 5º pergunta")
    RC += 1
else:
    print(f"Errou a 5º pergunta, a resposta correta era {a5 + b5}")

if RC == 5:
    print("Você acertou todas as perguntas 5 de 5")
elif 0 < RC < 5:
    print(f"Você acertou {RC} de 5 perguntas")
else:
    print("Você errou todas as perguntas 0 de 5")