from random import randint
from time import sleep
from operator import itemgetter

jogadores = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)}

print('-='*30)
print('SORTEANDO VALORES')
sleep(1)
for k, v in jogadores.items():
    print(f'{k} tirou {v}')
    sleep(1)
print('-='*30)
print('\033[1;35mRanking dos jogadores\033[m')
print('-='*30)

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]} ')
    sleep(1)