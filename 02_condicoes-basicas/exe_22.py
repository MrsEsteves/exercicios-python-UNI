"""
Escreva um programa que leia o ano de nascimento de um rapaz e mostre a sua
situação em relação ao alistamento militar. - Se estiver antes dos 18 anos, mostre em
quantos anos faltam para o alistamento. - Se já tiver depois dos 18 anos, mostre quantos
anos já se passaram do alistamento.
"""

ano = int(input("Digite o ano de nascimento do rapaz: "))
idade = 2026 - ano

if idade < 18:
    print(f"Faltam {18 - idade} anos para o seu alistamento.")
elif idade == 18:
    print("Você já pode se alistar.")
else:
    print(f"Se passaram {idade - 18} anos do seu alistamento.")
