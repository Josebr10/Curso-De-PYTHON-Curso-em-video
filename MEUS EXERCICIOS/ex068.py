from random import randint
print('-=-'*10)
print('VAMOS JOGAR \033[1;35mPAR\033[m OU \033[1;36mIMPAR\033[m')
print('-=-'*10)
vencer = 0
while True:
    computador = randint(0,10)
    n = int(input('Digite seu numero: '))
    par_impar = str(input('Voce escolhe Par ou Impar [P/I]: ')).upper().strip()[0]
    print('-=-'*10)
    soma = computador + n
    if soma % 2 == 0:
        print('-' * 20)
        print(f'O computador escolheu {computador} e voce {n}')
        print('-' * 20)
        print(f'O Total de {soma} DEU \033[1;35mPAR\033[m')
        if par_impar == 'P':
            print('\033[1;32m Voce ganhou!\033[m')
            print('Vamos jogar novamente...!')
            print('-=-'*10)
        elif par_impar == 'I':
            print('-=-' * 10)
            print('\033[1;31mVOCE PERDEU!\033[m')
            print('-=-' * 10)
            break
    elif soma % 2 != 0:
        print('-' * 20)
        print(f'O computador escolheu {computador} e voce {n}')
        print('-' * 20)
        print(f'O Total de {soma} DEU \033[1;36mIMPAR\033[m')
        if par_impar == 'I':
            print('\033[1;32mVOCE GANHOU!!\033[m')
            print('Vamos jogar novamente...!')
            print('-=-'*10)
        elif par_impar == 'P':
            print('-=-'*10)
            print('\033[1;31mVOCE PERDEU!\033[m')
            print('-=-' * 10)
            break
    vencer+=1
print(f'\033[1;31mGAME OVER!\033[m voce venceu \033[1;32m{vencer}\033[m vezes')