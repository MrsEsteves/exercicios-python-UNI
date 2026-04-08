"""
Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse
80Km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o
valor da multa, cobrando R$5 por cada Km acima da velocidade permitida.
"""

v = float(input("Qual a velocidade do carro?: "))

if v > 80:
    print(f"Você foi multado. \nO valor da multa é de R${(v - 80) * 5}")
else:
    print("Nenhuma multa recebida.")
