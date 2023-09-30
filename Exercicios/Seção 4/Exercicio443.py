"""
Exercicio 43: Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:
- O total a pagar com desconto de 10%
- O valor de cada parcela, no parcelamento de 3x sem juros;
- A comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto)
- A comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)
"""

print("Por favor informe o valor da compra")

while True:
    try:
        VC = float(input())
        if not -10000000 <= VC <= 10000000:
            raise ValueError("Este numero é muito grande por favor digite um numero menor.")
    except ValueError as e:
        print("Valor inválido, por favor digite apenas numeros.")
    else:
        break

print("Vamos resumir essa compra para você")

D = (VC/100) * 10
AV = VC - D
P = VC/3
CVAV = (AV/100) * 5
CVP = (VC/100) * 5

print(f"Caso seja pago a vista ficara: R${AV:.2f}")
print(f"Caso seja parcelado ficara 3x parcelas de R${P:.2f}")
print(f"A comissão do vendedor caso seja a vista é R${CVAV:.2f}")
print(f"A comissão do vendedor caso seja parcelado é R${CVP:.2f}")
