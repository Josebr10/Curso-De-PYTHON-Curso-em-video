#variavel.append('informacao') adiciona um item na lista
#variavel.insert(0,'item') adiciona um item em um lugar especifico na lista
# del variavel[3] deleta o item 3 da lista
# lanche.pop(3) ou lanche.pop() deleta o 3 da lista tbm \\ MAS E UTILIZADO PARA DELETAR O ULTIMO ITEM DA LISTA
# variavel.remove('item') remove o conteudo com o nome dele

#valores.sort() ordena em ordem crescente os valores

#valores.sort(reverse=True) ordem em ordem decrecente os valores

#len(valores) le os numeros de componentes da lista(0,1,2,3,4,5,6)

num = [2,5,9,1]
num[0]=3
num[3]=6
num.append(7) #ADICIONEI O NUMERO 7 NO ELEMENTO
num[4]=10
num.sort() #ADICIONEI A SEQUENCIA DO MAIOR PARA O MENOR
num.reverse() #ADICIONEOI A SEQUENCIA DO MAIOR PARA O MENOR
num.insert(2,34) # ELE ADICIONA NA POSICAO O NUMERO SOLICITADO
del num[2] #REMOVE O NUMERO SOLICITADO
num.pop() #REMOVE O ULTIMO ITEM DA LISTA
num.pop(2) #REMOVE  O ELEMENTO NUMERO 2 DA LISTA
num.insert(2,2) #INSERE O NUMERO NO LUGAR QUE VOCE SELECIONOU
num.insert(4,2)
num.remove(2) #SO VAI REMOVER UM UNICO NUMERO QUE VOCE SELECIONOU, SO UM DE UMA LISTA INTEIRA
num.insert(5,2)
if 4 in num:
    num.remove(4)
else:
    print('Nao tem numero 4 na lista')
print(num)
print(f'\033[1;32mEssa lista tem {len(num)} elementos\033[m')



valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for c, v in enumerate(valores): #O ENUMERATE() COLOCA A POSICAO INICIAL DA SEQUENCIA // EX: POSICAO 0 = 3 / POSICAO 1 = 2 \ POSICAO 2 = 3

    print(f'\nNa posicao {c} encontrei o valor {v}...',end='') #end='' DEIXA NA MESMA LINHA
print(valores)
print('Cheguei no final da lista')

numeros = list()
for cont in range (0,6):
    numeros.append(int(input('Digite um numero inteiro: ')))
for c, v in enumerate(numeros):
    print(f'Na posicao {c} encontrei o valor {v}...')

a = [2, 3, 4 , 7]
b = a[:] #FAZ COM QUE B RECEBA TODOS OS ELEMENTOS DE A, MAS NAO VAI ALTERA A QND FOR EDITAR OU REMOVER ALGO
b[2]= 8
print(f'A lista A: {a}')
print(f'A lista B: {b}')