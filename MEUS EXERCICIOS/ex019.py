import random

n1= input ('Primeiro aluno: ')
n2= input('Segundo Aluno: ')
n3= input('Terceiro Aluno: ')
n4= input('Quarto Aluno: ')
alunos=[n1,n2,n3,n4]
sorteio=random.choice(alunos)

print(f'O aluno escolhido foi: {sorteio}')

