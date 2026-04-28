#for c in range(1,6): #vai ate 5
#  print(c)
#print('FIM')

#for c in range(6,0,-1): #vai de 6 pra baixo
    #print(c)
#print('FIM')

i = int(input('inicio: '))
f = int(input('fim: '))
p = int(input('passe: '))
for c in range(i,f,+p):
    print(c)
print('FIM')

for c in range(0,3):
    n = int(input('digite um numero: '))
print('fim')

s = 0
for c in range(0,5):
    n = int(input('Digite um numero: '))
    s += n
print (f'A soma de todos os numeros e igual a: {s}')