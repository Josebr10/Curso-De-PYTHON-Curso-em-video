from random import randint
numeros =  (randint(0,10),randint(0,10),randint(0,10),
      randint(0,10),randint(0,10))
print(f'Os numeros sorteados foram: ',end=' ')
for n in numeros:
    print(f'{n} ',end=" ")


print(f'\nO Maior valor sorteado foi: \033[1;32m{max(numeros)}\033[m')
print(f'O Menor valor sorteado foi: \033[1;31m{min(numeros)}\033[m')