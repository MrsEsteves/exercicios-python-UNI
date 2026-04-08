"""
[DESAFIO] Refaça o algoritmo 25, acrescentando o recurso de mostrar que tipo de
triângulo será formado: - EQUILÁTERO: todos os lados iguais - ISÓSCELES: dois lados iguais
- ESCALENO: todos os lados diferentes
"""

a = float(input("Valor de segmento a: "))
b = float(input("Valor de segmento b: "))
c = float(input("Valor de segmento c: "))

if (a < b + c) and (b < a + c) and (c < a + b):
    print("É possível formar um triângulo com essas retas.")
    if a == b == c:
        print("Será um triangulo equilátero")
    elif a == b or b == c or a == c:
        print("Será um triangulo isosceles")
    else:
        print("Será um triangulo escaleno")
else:
    print("Não é possível criar um triângulo com essas retas.")
