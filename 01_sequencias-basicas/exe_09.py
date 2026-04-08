"""
Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$) e
mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,45.
"""

r = float(input("Digite a quantidade de dinheiro que tem na carteira: "))

print(f"Você pode comprar {r / 3.45:g} dólares.")
