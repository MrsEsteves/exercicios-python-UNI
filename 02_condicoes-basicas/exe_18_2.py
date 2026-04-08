"""
Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade dela
e depois mostre se ela pode ou não votar.
"""

# Contando com o dia e mês de nascimento do usuario

# Dados de hoje
d_atual = 8
m_atual = 4
a_atual = 2026

# Usuario
d_nasc = int(input("Em que dia você nasceu?: "))
m_nasc = int(input("Em que mês você nasceu? (1 a 12): "))
a_nasc = int(input("Em que ano você nasceu?: "))

idade = a_atual - a_nasc

if m_atual < m_nasc:
    idade -= 1
elif m_atual == m_nasc:
    if d_atual < d_nasc:
        idade -= 1

if idade >= 18:
    print("Você pode votar")
else:
    print("Você não pode votar ainda")
