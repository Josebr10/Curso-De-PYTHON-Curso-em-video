estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf']= str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())    #.copy ADICIONA OS ELEMENTOS DE UM DICIONARIO A UMA LISTA
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem o valor {v}')
    for v in e.values():
        print(v, end=' ')
    print()