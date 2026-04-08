"""
[DESAFIO] Escreva um programa para calcular a redução do tempo de vida de um
fumante. Pergunte a quantidade de cigarros fumados por dias e quantos anos ele já
fumou. Considere que um fumante perde 10 min de vida a cada cigarro. Calcule quantos
dias de vida um fumante perderá e exiba o total em dias.
"""

q_cig = int(input("Qual a quantidade de cigarros que fuma por dia?: "))
anos = int(input("A quantos anos fuma?: "))

print(
    f"O fumante perderá aproximadamente {((q_cig * (anos * 365)) * 10) / 1440:.3f} dias de vida"
)
