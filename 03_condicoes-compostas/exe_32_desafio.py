"""
[DESAFIO] Crie um jogo onde o computador vai sortear um número entre 1 e 5 o
jogador vai tentar descobrir qual foi o valor sorteado.
"""

import random

pc = random.randint(1, 5)
n = int(input("Adivinhe o numero: "))

if n == pc:
    print("Você acertou")
else:
    print(f"Você errou, o numero era {pc}")
