nome = str(input('Qual é o seu nome?'))
if nome == 'jose':
    print('Que nome bonito!')
elif nome == 'paulo' or 'joao' or 'maria':
    print('Seu nome é bem popular no Brasil')
elif nome in 'julia ana claudia felipa clara':
    print('Que nome feminino mais bonito')
else:
    print ('Que nome comum')
print(f'Tenha um otimo dia {nome}')