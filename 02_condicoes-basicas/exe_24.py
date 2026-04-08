"""
Faça um algoritmo que pergunte a distância que um passageiro deseja percorrer em
Km. Calcule o preço da passagem, cobrando R$0.50 por Km para viagens até 200Km e
R$0.45 para viagens mais longas.
"""

d = float(input("Qual a distancia que deseja percorrer?: "))

if d > 200:
    print(f"O preço da passagem é de R${d * 0.45}.")
else:
    print(f"O preço da passagem é de R${d * 0.50}.")
