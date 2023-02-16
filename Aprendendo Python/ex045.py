from random import randint


itens = ('PEDRA','PAPEL','TESOURA')

jogador = int(input('Suas Opções: \n[0] - PEDRA\n[1] - PAPEL\n[2] - TESOURA\nQual é sua Jogada? '))
computador = randint(0,2)
print('='*11)
print('O computador escolheu {}'.format(itens[computador]))
print('jogador escolheu {}'.format(itens[jogador]))
print('='*11)

if computador == jogador:
    print('EMPATE')
elif computador == 0:
    if jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
            print('COMPUTADOR VENCEU')
elif computador == 1:
    if jogador == 2:
        print('JOGADOR VENCEU')
    elif jogador == 0:
        print('COMPUTADOR VENCEU')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
else:
    print('jogada inválida')