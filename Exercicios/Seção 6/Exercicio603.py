"""
Exercicio 3: Faça um algoritmo utilizando o comando while que mostra uma contagem regressiva na tela,
iniciando em 10 e terminando em 0. Mostrar uma mensagem "FIM!" após a contagem.
"""

print("Iniciando contagem regressiva!")

N = 11

while N > 0:
    N -= 1
    print(N)
    if N == 0:
        print("FIM!")
