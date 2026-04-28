a = int(input('Primeiro Valor: '))
b = int(input('Segundo Valor: '))
c = int(input('Terceiro Valor: '))
menor = a
if b<a and b < c:
    menor=b
if c<b and c < a:
    menor=c
maior = c
if a>b and a>c:
    maior = a
if b>c and b>a:
    maior = b
medio = b
if a>b and a<c:
    medio=a
if c>a and c<b:
    medio = b

print (f'O menor valor foi:{menor}\n ')
print(f'O maior valor foi:{maior}')
print(f'O valor do meu foi: {medio}')
