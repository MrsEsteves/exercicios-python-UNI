"""
[DESAFIO] Crie um jogo onde o computador vai sortear um número entre 1 e 5 o
jogador vai tentar descobrir qual foi o valor sorteado.
"""

# Usando While e tentativas

import random

pc = random.randint(1, 5)
tentativa = 0

while True:
    n = int(input("Adivinhe o numero: "))
    tentativa += 1

    if n == pc:
        print("Acertou")
        break
    else:
        print("Errou. Tente de novo")

    if tentativa == 3:
        print(f"Tentativas excedidas. O numero era {pc}")
        break
