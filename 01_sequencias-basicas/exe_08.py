"""
Desenvolva um programa que leia uma distância em metros e mostre os valores
relativos em outras medidas.
Ex: Digite uma distância em metros: 185.72 A distância de 85.7m
corresponde a: 0.18572Km 1.8572Hm 18.572Dam 1857.2dm 18572.0cm
185720.0mm
"""

d = float(input("Digite uma distância em metros: "))

print(
    f"A distancia de {d} corresponde a: {d / 1000:g}Km {d / 100:g}Hm {d / 10:g}Dam {d * 10:g}dm {d * 100:g}cm {d * 1000:g}mm"
)
