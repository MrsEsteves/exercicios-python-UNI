"""
Faça um algoritmo que leia o salário de um funcionário, calcule e mostre o seu novo
salário, com 15% de aumento.
"""

s = float(input("Digite o salário do funcionário: "))

print(f"O novo salário será de {s + ((s * 15) / 100)}")
