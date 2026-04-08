"""
[DESAFIO] Crie um jogo onde o computador vai sortear um número entre 1 e 5 o
jogador vai tentar descobrir qual foi o valor sorteado.
"""

# Usando While

import random

pc = random.randint(1, 5)

while True:
    n = int(input("Adivinhe o numero: "))

    if n == pc:
        print("Acertou")
        break
    else:
        print("Errou. Tente de novo")
