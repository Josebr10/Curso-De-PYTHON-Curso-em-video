import math

co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
h  = math.hypot(co,ca)
print (f'A hipotenusa da operacao e: {h:.2f}')
