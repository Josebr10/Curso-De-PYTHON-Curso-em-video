'''for c in range(1,10+1):    #USANDO FOR
    print(c)
print('FIM')'''


'''c = 0    #USANDO WHILE
while c < 10:
    c += 1
    print(c)
print("FIM")'''


'''for c in range(1, 5):
    n = int(input('Digite um valor: '))
print('fim')'''

'''n = 1
while n != 0:
    n = int(input('Digite um valor: '))
    print('fim')'''

'''s = 'sim'
while s != 'sim':
    s = str(input('digite uma palavra: '))
    u = str(input('quer continuar? [sim/nao]: ')).lower()
    print('fim')'''

'''n = 1
while n <= 10:
    print(n)
    n = n + 1
print('fim')'''

sexo = ['M','F']
while sexo != 'M' and sexo != 'F':
    usuario = str(input('Digite seu nome: '))
    sexo = str(input(f'Ola {usuario}, Qual e o seu sexo? [M/F]: ')).upper()
    if sexo == 'M':
        print('Voce e um HOMEM')
    elif sexo == 'F':
        print('Voce e uma MULHER!')
    else:
        print('Sexo invalido! Digite novamente!')
print('FIM')