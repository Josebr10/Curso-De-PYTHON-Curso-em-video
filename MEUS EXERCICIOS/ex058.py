from time import sleep
from random import randint
print('-=-' * 20)
print('Vou pensar em um numero de 0 ate 10... Tente Adivinhar!')
print('-=-'*20)
computador = randint(0,10)
escolha = int(input('Escolha um numero entre 0 e 10: '))
tentativas = 0
#acertou = False ----> while not acertou:
while escolha != computador:
    computador = randint(0, 10)
    tentativas += 1
    escolha = int(input('Errou! escolha outro numero entre 0 e 10: '))
    if escolha == computador:
        print(f'\033[1:32mVOCE ACERTOU !!\033[m\nEU PENSEI NO NUMERO:\033[1:35m {computador} \033[m\nVOCE PENSOU NO NUMERO:\033[1:36m {escolha} \033[m')
        print(f'VOCE PRECISOU DE \033[1:32m{tentativas} TENTATIVAS!\033[m')

print('OBRIGADO POR JOGAR!')
