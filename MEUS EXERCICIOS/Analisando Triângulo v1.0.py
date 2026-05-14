print ('-=-'*20)
print ('\033[1;33m Analisador de Triangulos \033[m')
print('-=-'*20)
t1 = float(input('\033[1;32m Primeiro segmento\033[m: '))
t2 = float(input('\033[1;34m Segundo Segmento\033[m: '))
t3 = float(input('\033[1;35m Terceiro Segmento\033[m: '))
if t1 < t2 + t3 and t2 < t1 + t3 and t3 < t1 + t2:
    print('Os seguimentos a cima PODEM FORMAR UM TRIANGULO: ')
else:
    print('Os seguimentos a cima NAO PODEM FORMAR UM TRIANGULO:')