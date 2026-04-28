times = ['Palmeiras','Sao Paulo','Fluminense','Flamengo','Bahia',
         'Atletico Paranaense','Coritiba','Atletico Mineiro','Red bull Bragantino'
    ,'Botafogo','Gremio','Vasco','Internacional','Vitoria','Santos','Corinthians',
         'Chapecoence','Clube do Remo','Cruzeiro','Mirassol']
print("-="*20)
#for t in times:   ESSE AQUI E PARA COLOCAR EM SEQUENCIA DE CIMA PRA BAIXO
    #print(t)
print(f'Os Times da Serie A sao: {times}')
print("-="*20)
print(f'Os 5 primeiros times sao {times[0:5]}')
print("-="*20)
print(f'Os 4 Ultimos sao: {times[-4:]}')
print("-="*20)
print(f'Times em Ordem Alfabetica: {sorted(times)}')
print("-="*20)
print(f'O Chapecoence esta na colocacao: {times.index("Chapecoence")+1} Posicao')