from random import randint

print('-'*40)
print('JOGA NA MEGA SENA'.center(40))
print('-'*40)
lista = list()
jogo = list()

quantidade = int(input('Quantos jogos voce quer eu sorteie ? '))
total = 1
while total <= quantidade:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogo.append(lista[:])
    lista.clear()
    total += 1

print('-=' * 3, f'SORTEANDO {quantidade} NUMEROS DA MEGASENA', '-='*3)
for i, l in enumerate(jogo):
    print(f'Jogo {i+1} sorteado {l}')

