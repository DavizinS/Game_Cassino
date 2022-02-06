"""
[JOGO 1]
Irei criar um sistema de jogos de azar...

[1] Times de Futebol
[2] Roleta
"""
from sis import *

while True:
    titulo('SPORTING BETS')
    op = opc()
    if op == 1:
        bras()
    elif op == 2:
        roleta()
    elif op == 3:
        saldo(dinheiro=30)
    elif op == 4:
        print(f'Você está saindo...')
        sleep(0.7)
        break
