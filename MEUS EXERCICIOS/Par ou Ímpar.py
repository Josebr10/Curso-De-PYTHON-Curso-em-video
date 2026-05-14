from time import sleep
print('-=-'* 20)
numero = int(input('Me diga um numero qualquer: '))
resultado = numero % 2
print('ESPERANDO...')
sleep(2)
if resultado == 0:
    print(f'O numero {numero} e PAR!')
else:
    print(f'O Numero {numero} e IMPAR!')

