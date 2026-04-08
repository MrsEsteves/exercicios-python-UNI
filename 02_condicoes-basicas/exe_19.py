"""
Crie um algoritmo que leia o nome e as duas notas de um aluno, calcule a sua média
e mostre na tela. No final, analise a média e mostre se o aluno teve ou não um bom
aproveitamento (se ficou acima da média 7.0).
"""

nome = input("Qual o nome do aluno?: ")
nota1 = float(input("Digite a primeira nota (0 a 10): "))
nota2 = float(input("Digite a segunda nota (0 a 10): "))

media = (nota1 + nota2) / 2

if media > 7.0:
    print(f"O aluno {nome} teve um bom desempenho.")
else:
    print(f"O aluno {nome} não teve um bom desempenho.")
