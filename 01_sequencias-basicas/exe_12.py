"""
Crie um programa que leia o preço de um produto, calcule e mostre o seu PREÇO
PROMOCIONAL, com 5% de desconto.
"""

p = float(input("Digite o preço do produto: "))

print(f"O preço promocional deste produto é de {p - ((p * 5) / 100)}")
