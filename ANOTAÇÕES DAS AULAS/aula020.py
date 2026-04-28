def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')



soma (3, 5)
soma (5, 9)
soma (9, 17)

def contador(* num):
    for valor in num:
        print(f'{valor}', end='')
    print('fim')


contador(1, 7, 8)
contador(3, 8, 3, 6)
contador(6, 1)
contador(14, 23, 1, 4, 6, 65)

def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e sao ao todo {tam}')

contador(1, 7, 8)
contador(3, 8, 3, 6)
contador(6, 1)
contador(14, 23, 1, 4, 6, 65)

def dobra( lst  ):
    pos = 0
    while pos < len(lst):
        lst[pos]*= 2  #A lista na posicao "*" pega a posicao atual da lista
        pos += 1

valores = [6, 3, 9, 1, 0, 2]
dobra (valores)
print(valores)


def some(* valores):
    s = 0
    for num in valores:
        s += num
        print(f'Somando os valores {valores} temos {s}')


some(8, 9)
some (4, 5, 8)
some (3,6, 12)