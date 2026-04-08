"""
A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva um
programa que pergunte a quantidade de Km percorridos por um carro alugado e a
quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar, sabendo
que o carro custa R$90 por dia e R$0,20 por Km rodado.
"""

q_km = float(input("Quantos km percorreu o carro?: "))
q_dias = int(input("Por quantos dias ele foi alugado?: "))

print(f"O preço total a se pagar é de {(q_km * 0.20) + (q_dias * 90)}")
