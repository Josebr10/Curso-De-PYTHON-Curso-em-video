print('Gerador de PA')
print('-=-'*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input(' Razao da PA:'))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print (f'{termo} -->', end=' ')
        termo += razao
        cont += 1
    print ('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar a mais? '))

    print('-=-'*10)
print(f'Voce mostrou \033[1;32m {total} termos \033[m')
print('FIM')