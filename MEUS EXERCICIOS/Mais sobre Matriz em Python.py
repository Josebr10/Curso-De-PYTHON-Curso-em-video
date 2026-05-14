valores = list()
pares = list()

for c in range (3):
    numero = int(input(f"Digite um valor para [0] [{c}]: "))
    valores.append(numero)
    if numero % 2 == 0:
        pares.append(numero)


for c in range (3):
    numero1 = int(input(f"Digite um valor para [1] [{c}]: "))
    valores.append(numero1)
    if numero1 % 2 == 0:
        pares.append(numero1)


for c in range (3):
    numero2 = int(input(f"Digite um valor para [2] [{c}]: "))
    valores.append(numero2)
    if numero2 % 2 == 0:
        pares.append(numero2)

print('-='*30)
print(f'[  {valores[0]}  ] [  {valores[1]}  ]  [  {valores[2]}  ]')
print(f'[  {valores[3]}  ] [  {valores[4]}  ]  [  {valores[5]}  ]')
print(f'[  {valores[6]}  ] [  {valores[7]}  ]  [  {valores[8]}  ]')
print('-='*30)



print(f'A soma dos valores Pares e :{sum(pares)}')
print(f'A soma dos valores da terceira coluna é: {valores[2] + valores [5] + valores [8]}')