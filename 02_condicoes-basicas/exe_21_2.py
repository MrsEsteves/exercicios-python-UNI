# Faça um algoritmo que leia um determinado ano e mostre se ele é ou não BISSEXTO.

# Usando biblioteca calendar

import calendar

ano = int(input("Digite o ano: "))

if calendar.isleap(ano):
    print(f"O ano {ano} é bissexto")
else:
    print(f"O ano {ano} não é bissexto")
