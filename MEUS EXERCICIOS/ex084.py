info = list()
dados = list()
peso = list()

while True:
    dados.append(str(input('Digite um Nome: ')))
    dados.append(float(input('Digite um Peso: ')))
    info.append(dados[:])
    peso.append(dados[1])
    dados.clear()
    print('\033[1;32mCadastrado com sucesso!\033[m')

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Voce deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        break
    print('-='*20)
print('\033[1;35m-=\033[m'*25)

menor = min(peso)
maior = max(peso)

print(f'O numero de pessoas cadastradas foi {len(info[0:])}')
print(f'O menor peso foi de {menor} KG. Peso de:', end=' ')
for pessoa in info:
    if pessoa[1] == menor:
        menor = pessoa[1]
        print(f'{pessoa[0]}',end=', ')

print()
print(f'O maior peso foi {maior} KG. Peso de:',end=' ')
for pessoa in info:
    if pessoa[1] == maior:
        maior = pessoa[1]
        print(f'{pessoa[0]}', end=', ')













