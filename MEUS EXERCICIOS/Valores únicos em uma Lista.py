lista = []

while True:
    valor = int(input('\033[1:36mDigite um Valor: \033[m'))

    if valor in lista:
        print('\033[1:31mErro!Esse valor ja esta na lista!\033[m')

    else:
        lista.append(valor)
        print('\033[1:32mNumero Adicionado com sucesso!\033[m')

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [\033[1:32m S \033[m/\033[1:31m N \033[m] ')).strip().upper()[0]
    if continuar == 'N':
        break

print('-='*25)
print('\033[1:35m BANCO DA SUA LISTA\033[m'.center(60,'='))
print('-='*25)
lista.sort()
print(f'\033[1;34m Os numeros Adicionados da sua lista sao \033[m \033[1;32m{lista}\033[m')
