galera = list()
pessoa = dict()
soma = media = 0
mulheres = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            if pessoa['sexo'] == 'F':
                mulheres += 1
            break
        print('ERRO! Responda apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resposta = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resposta == 'N':
        break
print('-='*30)
print(f' A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f' B) A media de idade das pessoas e de {media:5.2f} Anos')
print(f'C) {mulheres} Mulheres Foram cadastradas')
print(f'D) As Mulheres cadastradas Foram ', end=' ')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]},', end=' ')
print()
print(f'Pessoas que estao acima da media: ')
for p in galera:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ',end='')
        print()
print('<<FECHADO>>')
