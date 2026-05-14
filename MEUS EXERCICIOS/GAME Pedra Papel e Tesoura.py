from random import randint
from time import sleep
print ('-=-' * 10, 'JOKENPO', '-=-' * 10)
print('''[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
itens = ('PEDRA','PAPEL','TESOURA')

print('-=-'* 23)
jogador = int(input('Qual a sua escolha? '))
if jogador >= 3:
    print('JOGADA INVALIDA')
    exit()

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
computador = randint(0,2)

print('-=-'*23)

print(f'VOCE ESCOLHEU: \033[1:34m{(itens[jogador])} \033[m')

print(f'O COMPUTADOR ESCOLHEU: \033[1:35m{(itens[computador])} \033[m')

print('-=-'*23)


if computador == jogador:
    print('\033[1:33m O JOGO DEU EMPATE\033[m ')

elif (jogador == 0 and computador == 2) or \
        (jogador == 1 and computador == 0) or \
        (jogador == 2 and computador == 1):
    print('\033[1:32m VOCE GANHOU!!\033[m ')
else:
    print('\033[1:31m VOCE PERDEU! \033[m ')