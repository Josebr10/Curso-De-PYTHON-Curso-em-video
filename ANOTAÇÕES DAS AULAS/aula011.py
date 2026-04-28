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