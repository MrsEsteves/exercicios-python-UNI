# [DESAFIO] Crie um jogo de JoKenPo (Pedra-Papel-Tesoura)

import random

itens = ("Pedra", "Papel", "Tesoura")
computador = random.randint(0, 2)

if computador == 0:
    print("Pedra")
elif computador == 1:
    print("Papel")
else:
    print("Tesoura")
