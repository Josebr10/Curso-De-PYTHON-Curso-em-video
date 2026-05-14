par = list()
impar = list()
valores = list()

while True:
    valores.append(int(input('Digite um valor: ')))
    if valores[-1] % 2 == 0:
        par.append(valores[-1])
    if valores[-1] % 2 == 1:
        impar.append(valores[-1])
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-='*30)
print('\033[1;34m-=\033[m'* 50)
print(f'A lista completa e: {valores}')
print(f'A lista de pares e : {par}')
print(f'A lista de impares e: {impar}')