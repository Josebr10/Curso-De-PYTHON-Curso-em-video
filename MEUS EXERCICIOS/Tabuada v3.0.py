while True:
    print('-=-' * 20)
    n = int(input('Deseja a tabuada de qual valor? '))
    if n < 0:
        break
    print ('-'*30)
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
print('-'*30)
print('\033[1;31mPROGRAMA DE TABUADA ENCERRADO!\033[m \n\033[1;32mVOLTE SEMPRE!\033[m')
print('-'*30)
