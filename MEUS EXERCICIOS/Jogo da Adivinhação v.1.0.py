from random import randint #biblioteca para randomizar
from time import sleep #biblioteca para temporizar
computador = randint(0, 5) #faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um numero de 1 ate 5... Tente Adivinhar!')
print('-=-'*20)
jogador = int(input('Em que numero eu  Pensei? '))
print('PROCESSANDO SUA RESPOSTA...')
sleep(2) #faz o computador esperar 3 segundos
if jogador == computador:
    print(f'Voce acertou!!! Eu tambem pensei em {computador}')
else:
    print(f'EU GANHEII!!\n Eu pensei no numero {computador} e nao no {jogador}')
