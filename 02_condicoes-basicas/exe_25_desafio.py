"""
[DESAFIO] Crie um programa que leia o tamanho de três segmentos de reta. Analise
seus comprimentos e diga se é possível formar um triângulo com essas retas.
Matematicamente, para três segmentos formarem um triângulo, o comprimento de cada
lado deve ser menor que a soma dos outros dois.
"""

a = float(input("Valor de segmento a: "))
b = float(input("Valor de segmento b: "))
c = float(input("Valor de segmento c: "))

if (a < b + c) and (b < a + c) and (c < a + b):
    print("É possível formar um triângulo com essas retas.")
else:
    print("Não é possível criar um triângulo com essas retas.")
