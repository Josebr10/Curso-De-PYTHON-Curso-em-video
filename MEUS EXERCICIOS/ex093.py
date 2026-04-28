nome = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {nome} jogou?:  '))

informacoes = {
    'nome':nome,
    'partidas':partidas
}

gols= []

for c in range(informacoes["partidas"]):
    gol = int(input(f"Quantos gols o {nome} fez na {c+1} partida?: "))
    gols.append(gol)

informacoes["gols"] = gols  #   SALVEI UMA VARIAVEL EM UM DICIONARIO
print('-='*30)
print(informacoes)
print('-='*30)


for k,v in informacoes.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)

print(f'O jogador {nome} jogou {partidas} partidas')
for c in range(informacoes["partidas"]):
    print(f'Na partida {c+1}, ele fez {gols[c]} gols')