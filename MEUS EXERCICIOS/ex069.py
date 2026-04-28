maior_idade = 0
homem = 0
mulher = 0
cont = 0
while True:
    print('='*30)
    print('_____CADASTRE UMA PESSOA_____')
    print('='*30)
    idade = int(input('Idade: '))
    if idade > 18:
        maior_idade += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'M':
        homem += 1
    elif sexo == 'F':
        if idade < 20:
                mulher += 1
    print('-'*30)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'S':
        cont += 1
    if continuar == 'N':
        cont += 1
        break

print('\033[1;31mFIM DO PROGRAMA\033[m')
print(f'Voce cadastrou {cont} pessoas')
print (f'Voce cadastrou {homem} homens')
print(f'Voce cadastrou {mulher} mulheres abaixo dos 20 anos')
print(f'Total de pessoas com mais de 18 anos: {maior_idade}')
