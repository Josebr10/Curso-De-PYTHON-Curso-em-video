valores = []
while True:
    valores.append(int(input('Digite um Valor: ')))

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print('-='*30)
print(f'Voce digitou {len(valores)} elementos')
print(f'Os valores em ordem decrescente sao {sorted(valores,reverse=True)}') #DEIXAR EM ORDEM DECRESCENTE
len(valores)
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 nao faz parte da lista!')

#MANEIRA MAIS FACIL DE DEIXAR O VALOR EMM ORDEM DECRESCENTE

####################    valores.sorted(reverse=True)   ##############################