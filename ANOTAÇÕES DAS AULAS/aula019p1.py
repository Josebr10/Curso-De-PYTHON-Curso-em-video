pessoas = { 'nome':'Jose' , 'idade': 20 , 'sexo': 'Masculino'}
print(pessoas)
print(pessoas['nome'])
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos e se considera {pessoas["sexo"]}')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k, v in pessoas.items():
    print(f'{k} = {v}')
del pessoas['sexo']
pessoas['nome'] = "Leandro"
pessoas["peso"] = 97
print(pessoas)


brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla':'RJ' }
estado2 = {'uf': 'Sao Paulo', 'sifla': 'SP' }
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['uf'])
print(brasil[1]['sigla'])


estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf']= str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())    #.copy ADICIONA OS ELEMENTOS DE UM DICIONARIO A UMA LISTA
print(brasil)