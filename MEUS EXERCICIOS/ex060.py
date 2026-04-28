#from math import factorial
#n = int(input('Informe um numero para calcular seu fatorial: '))
#f = factorial(n)
#print(f'O fatorial de {n} e:{f} ')
from time import sleep
n = int(input("Informe um numero para calcular sua fatoracao: "))
c = n
f = 1
print(f'Calculando {n}!...')
sleep(2)
while c > 0:
    print(f' {c} ', end='')
    print('x' if c > 1 else '=', end=' ')
    f *= c
    c -= 1
print(f)