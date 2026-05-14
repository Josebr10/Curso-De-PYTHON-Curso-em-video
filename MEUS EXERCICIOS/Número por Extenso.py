cont = ('zero','um','dois','tres','quatro','cinco',
        'seis','sete','oito','nove','dez','onze','doze',
        'treze','quatorze','quinze','dezeseis','dezesete',
        'dezoito','dezenove','vinte')
while True:
    tupla = int(input('Digite um numero entre \033[1;32m0 \033[me \033[1;32m20\033[m: '))
    if 0 <= tupla <= 20:
        print((f'Voce digitou o numero {cont[tupla]}'))
    else:
        print('\033[1;31mTente Novamente!\033[m')
    tupla = int(input('Digite um numero entre \033[1;32m0 e 20\033[m: '))

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        break
