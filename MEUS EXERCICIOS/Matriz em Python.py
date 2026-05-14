valores = list()
for c in range (3):
    numero = int(input(f"Digite um valor para [0] [{c}]: "))
    valores.append(numero)
for c in range (3):
    numero1 = int(input(f"Digite um valor para [1] [{c}]: "))
    valores.append(numero1)
for c in range (3):
    numero2 = int(input(f"Digite um valor para [2] [{c}]: "))
    valores.append(numero2)

print('-='*30)
print(f'[  {valores[0]}  ] [  {valores[1]}  ]  [  {valores[2]}  ]')
print(f'[  {valores[3]}  ] [  {valores[4]}  ]  [  {valores[5]}  ]')
print(f'[  {valores[6]}  ] [  {valores[7]}  ]  [  {valores[8]}  ]')