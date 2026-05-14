import random

n1= input('Primeiro aluno: ')
n2= input('Segundo aluno: ')
n3= input('Terceiro aluno: ')
n4= input('Quarto aluno: ')
nomes=[n1,n2,n3,n4]

random.shuffle(nomes)
print (f'Entre esses 4 alunos sorteados:\n {n1,n2,n3,n4}')
print(f'A sequecia de apresentacoes vai ser {nomes}')


