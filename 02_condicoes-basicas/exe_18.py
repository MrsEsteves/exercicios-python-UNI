"""
Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade dela
e depois mostre se ela pode ou não votar.
"""

ano = int(input("Digite o seu ano de nascimento: "))

idade = 2026 - ano

if idade >= 18:
    print("Você pode votar.")
else:
    print("Você não pode votar ainda.")
