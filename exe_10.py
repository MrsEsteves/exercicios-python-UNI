"""
Faça um algoritmo que leia a largura e altura de uma parede, calcule e mostre a área
a ser pintada e a quantidade de tinta necessária para o serviço, sabendo que cada litro
de tinta pinta uma área de 2metros quadrados.
"""

la = float(input("Digite a largura da parede: "))
a = float(input("Digite a altura da parede: "))

print(f"A área a ser pintada é de {la * a} metros quadrados.")
print(f"A quantidade necessária para o serviço é de {(la * a) / 2} litros de tinta.")
