"""
SISTEMAS DOS JOGOS
"""
import random
from time import sleep
from MeusDesafios.Cassino.interface import *

cor = ['\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;34m', '\033[1;35m', '\033[1;36m', '\033[1;37m', '\033[m']

"""
1 - Vermelho, 2 - Amarelo, 3 - Verde, ... Seguindo a tabela das cores em Python..
"""
times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense',
         'America-MG', 'Atlético-GO', 'Santos')
# Sistema do Brasileirão


def bras():
    while True:
        linha()
        print(f'{"":>20}{cores[2]}Bras{cor[1]}ilei{cor[2]}rão{cor[7]}')
        linha()
        for i, t in enumerate(times):
            print(f'\033[1m{"":>4}[{i}] {t}\033[m', end='')
            if i == 2:
                print('')
            elif i == 5:
                print('')
            elif i == 8:
                print()
        print()
        linha()
        resp = int(input('Número do time: ')[:2].strip())
        ntime = random.randint(0, 10)
        stime = times[ntime]
        if resp == ntime:
            print('Acertou.')
            print(f'Você ganhou acertou!')
        else:
            print('Errou.')
        print(f'Time sorteado foi o {stime}, N° {ntime}.')
        naposta = str(input('Deseja postar de novo? [S/N]: '))
        if naposta in 'Nn':
            print('OK... Até breve')
            sleep(1)
            break
        if naposta in 'Ss':
            print('Boa sorte! ^^ ')
        else:
            print(f'{cores[0]} Responda com S ou N.{cores[7]}')


# Sistema da roleta
rcor = ['V', 'R', 'B']
cgiros = 6


def roleta():
    linha()
    titulo('ROLETA BRASIL')
    linha()
    while True:
        escolha = int(input("""Escolha uma cor! 
        [ [1] - VERMELHO 
        [ [2] - ROXO 
        [ [3] - BRANCO: """))
        if escolha == 1:
            print(f'Você escolheu a cor {cores[0]}VERMELHO.{cores[7]}')
            break
        elif escolha == 2:
            print(f'Você escolheu a cor {cores[4]}ROXO.{cores[7]}')
            break
        elif escolha == 3:
            print(f'Você escolheu a cor \033[1mBRANCO.')
            break
        else:
            print('Opção inválida, escolha 1 ou 2.')
    giros = random.randint(1, cgiros)
    for g in range(1, giros+1):
        if rcor[0]:
            print(f'{cores[0]}|{cores[7]}', end=f'{cores[5]} > {cores[7]}')
            sleep(0.5)
        if rcor[1]:
            print(f'{cores[4]}|{cores[7]}', end=f'{cores[5]} > {cores[7]}')
            sleep(0.5)
        if rcor[2]:
            print(f'\033[1m|{cores[7]}', end=f'{cores[5]} > {cores[7]}')
            sleep(0.5)
        if g == giros:
            scor = random.choice(rcor)
            if scor == rcor[0]:
                print(f'{cores[0]}|{cores[7]}')
                print(f'A ultima cor foi {cores[0]}VERMELHA{cores[7]}')
                if escolha == 1:
                    print(f'\033[1;32mParabéns, você acertou!\033[1m')
                else:
                    print(f'\033[1;31mTente novamente.\033[m')
            if scor == rcor[1]:
                print(f'{cores[4]}|{cores[7]}')
                print(f'A ultima cor foi {cores[4]}ROXO{cores[7]}')
                if escolha == 2:
                    print(f'\033[1;32mParabéns, você acertou!\033[1m')
                else:
                    print(f'\033[1;31mTente novamente.\033[m')
            if scor == rcor[2]:
                print(f'\033[1m|{cores[7]}')
                print(f'A ultima cor foi \033[1mBRANCO{cores[7]}')
                if escolha == 3:
                    print(f'\033[1;32mParabéns, você acertou!\033[1m')
                else:
                    print(f'\033[1;31mTente novamente.\033[m')
    return
