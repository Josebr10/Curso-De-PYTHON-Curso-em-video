#PROGRAMA PARA CONTAGEM DE ESTOURO DE FOGOS DE ARTIFICIO
from time import sleep
print('-=-' * 20)
print ('\033[1:33m OS FOGOS DE ARTIFICIO VAO ESTOURAR EM 10 SEGUNDOS\033[m')
print('-=-' * 20)
tempo= 0
for c in range(10,-1, -1):
    print(c)
    sleep(1)
print ('-=-' * 20)
print('\033[1:32m FIM \033[m')
print('-=-' * 20)

