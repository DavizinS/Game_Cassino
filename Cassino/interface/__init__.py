"""
INTERFACE
"""
cores = ['\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;34m', '\033[1;35m', '\033[1;36m', '\033[1;37m', '\033[m']
"""
1 - Vermelho, 2 - Amarelo, 3 - Verde, ... Seguindo a tabela das cores em Python..
"""


def linha():
    print(f'{cores[1]}-{cores[7]}' * 60)


def titulo(nome):
    linha()
    print(f'{cores[0]}{nome:>34}{cores[7]}')
    linha()


def opc():
    print(f"""{cores[2]}
    {'':>15}[1] - Bras{cores[1]}ilei{cores[2]}rão{cores[7]}
    {cores[0]}{'':>15}[2] - Rol{cores[4]}eta{cores[7]}
    {cores[0]}{'':>15}[3] - {cores[3]} $ Saldo $ {cores[7]}
    {cores[0]}{'':>15}[4] - SAIR {cores[7]}\n""")
    while True:
        resp = int(input(f'{"":>19}{cores[1]}Digite uma opção: {cores[7]}'))
        if 0 < resp <= 4:
            break
        if resp > 3:
            print(f'{cores[0]}Opção inválida tente novamente.{cores[7]}')
    return resp


# Carteira #


def saldo(dinheiro):
    linha()
    titulo('Carteira')
    linha()
    print(f'Você tem R$ {dinheiro}.')
    return dinheiro
