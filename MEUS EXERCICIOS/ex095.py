time = list()
dados = dict()
partidas = list()

while True:
    dados.clear()
    dados['nome'] = str(input('Nome do Jogador: '))
    total = int(input(f'Quantas partidas {dados["nome"]} jogou: '))
    partidas.clear()
    for c in range(0, total):
        partidas.append(int(input(f'Quantos gols na partida {c+1}:  ')))
    dados['gols'] = partidas[:]
    dados['total'] = sum(partidas)
    time.append(dados.copy())
    while True:
        resposta = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resposta == 'N':
        break
print('-='*30)
print('cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? [999 para parar]: '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Nao existe Jogador com codigo {busca}')
    else:
        print(f' --- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'No jogo {i+1} fez {g} gols.')
    print('-'*40)
print('<<<VOLTE SEMPRE>>>')


