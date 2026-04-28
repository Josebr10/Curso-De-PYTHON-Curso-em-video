#\033[style;text;backm
#exemplo \033[0:33:44m
#style:0,1,4,7
#0= sem estilo,nada
#1=coloca o texto em negrito
#4=deixa o texto sublinhado
#7= tudo que coloca pra letra vai pra fundo e e o pra fundo vai pra letra

#text:30,31,32,33,34,35,36,37
#30=branco
#31=vermelho
#32=verde
#33=amarelo
#34=azul
#35=roxo
#36=ciano
#37=cinza

#cores para fundo
#back:40,41,42,43,44,45,46,47
#40=branco
#41=vermelho
#42=verde
#43=amarelo
#44=azul
#45=roxo
#6=ciano
#47=cinza

#back

print ('\033[0;30;41mTeste\033[m')
print ('\033[4;33;44mTeste\033[m')
print ('\033[0;35;43mTeste\033[m')
print ('\033[0;30;42mTeste\033[m')
print ('\033[mTeste\033[m')
print ('\033[7;30mTeste\033[m')

a = 3
b = 5
print (f'Os valores sao \033[1;32;40m{a}\033[m e \033[1;31;40m{b}\033[m')

nome = 'Jose'
print (f'Ola, muito prazer em te conhecer \033[4;34;40m{nome}\033[m!!')

cores = {'limpa'; '\033[m'
        'azul';'\033[34m'
'amarelo';'\033[33m'
'preto e branco';'\033[7;30m'}
