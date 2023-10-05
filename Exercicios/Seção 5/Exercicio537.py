"""
Exercicio 37: As tarifas de certo parque de estacionamento são as seguintes:
- 1º e 2º hora - R$1,00 cada
- 3º e 4º hora - R$1,40 cada
- 5º hora e seguintes - R$2,00 cada

O número de horas a pagar é sempre inteiro e arredondado por excesso. Deste modo,
quem estacionar durante 61 minutos pagará por duas horas, que é o mesmo que pagaria
se tivesse parmanecido 120 minutos. Os momentos de chegada ao parque e partida
deste são apresentados na forma de pares de inteiros, representando horas e minutos.
Por exemplo, o pai 12 50 representa "dez para a uma da tarde". Pretende-se criar um
programa que, lidos pelo teclado os momentos de chegada e de partida, escreva na tela
o preço cobrado pelo estacionamento. Admite-se que a chegada e a partida se dão com o intervalo
não superior a 24 horas. Portando, se uma dada hora de chegada for superior á de partida, isso
não é uma situação de erro, antes significará que a partida ocorreu no dia seguinte ao da chegada.
"""

print("Vamos calcular o quanto tera que pagar pelo uso do estacionamento")
HC = input("Digite a hora que chegou (hh mm): ").split()
HS = input("Digite a hora que saiu (hh mm): ").split()

MC = int(HC[0]) * 60 + int(HC[1])
MS = int(HS[0]) * 60 + int(HS[1])
Dif = MS - MC
HE = (Dif + 59) // 60

if HE <= 2:
    P = HE * 1.00
elif 3 <= HE <= 4:
    P = HE * 1.40
else:
    P = HE * 2.00

print(f"O valor total é de: R${P:.2f}")
