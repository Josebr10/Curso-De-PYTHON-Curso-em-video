teste = list()
teste.append('Jose')
teste.append(20)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = '22'
galera.append(teste[:])
print(galera)

tropa = [['jose',20],['isadora',20],['nitivix',20],['felipe',21]]
        #0            #1            #2             #3
print(tropa[1][0])

for pessoa in tropa:
    print(pessoa[0])
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')


familia = list()
dados = list()
totalmaior = totalmenor = 0

for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    familia.append(dados[:])
    dados.clear()

print(familia)
for pessoa in familia:
    if pessoa[1] >= 21:
       print(f'{pessoa[0]} e maior de idade  e tem {pessoa[1]} anos.')
       totalmaior += 1
    else:
        print(f'{pessoa[0]} e menor de idade e tem {pessoa[1]} anos de idade')
        totalmenor += 1

print(f'Os maiores de idade foram {totalmaior} maiores de idade.\n'
      f'E os menores de idade foram {totalmenor} menores de idade. ')
