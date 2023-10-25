"""
Exercicio 34: Faça um programa que calcule o menor número divisivel por cada um dos números de 1 a 20?
Ex: 2520 é o menor número que pode ser dividido por cada um dos números de 1 a 10, sem sobrar restoca
"""

MD = 1

for N in range(1, 21):
    DC = MD
    while DC % N != 0:
        DC += MD
    MD = DC

print(f"O menor número divisível por todos os números de 1 a 20 é {MD}.")
