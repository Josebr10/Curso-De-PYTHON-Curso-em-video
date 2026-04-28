frase='Curso em video python'


#fatiamento
#frase [5:9]


#Analise
len(frase)
#vai contar o comprimento da frase

frase.count('o')
#conta quantidades de 'o' na frase
frase.count('o',0,13)


frase.find('deo')
#Vai mostrar onde comecou a frase 'deo'

frase.find('android')
#se nao existir na frase, ela vai falar -1, pq nao foi encontrado

'Curso' in frase
#ele vai ver se tem na frase e vai colocar True ou false se estiver ou nao

#TRANSFORMACAO

frase.replace('Python','Android')
#substitui a frase pela outra nova


frase.upper()
#deixa a frase inteira em maiusculo

frase.lower()
#deixa a frase inteira em minusculo

frase.capitalize()
#ele deixa todos em minusculo mas o inicio ele deixa em maiusculo

frase.title()
#ele deixa as letras dos inicios de frases em maiusculo

frase.strip()
#remove todos os espacos inuteis

frase.rstrip()
#remove somente os ultimos espacos da direita

frase.lstrip()
#remove somente os primeiros espacos da esquerda


#DIVISAO
frase.split()
#ele pega os lugares com espacos e vai dividir eles, cada uma palavra vai ser uma nova lista, frase 1,2,3,4,...


'-'.join(frase)
#ele coloca esse ' - ' nos espacos das palavras, juntando as palavras, tipo, curso-em-video



