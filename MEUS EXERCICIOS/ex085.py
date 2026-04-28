valores = list()
impar = list()
par = list()
for c in range (1, 8):
   numero = int(input(f"Digite o {c} valor:"))
   valores.append(numero)
   if numero % 2 == 0:
       par.append(numero)
   elif numero % 2 == 1:
       impar.append(numero)

print('-=-'*30)
print(f'Voce Adicionou os Valores: \033[1;32m{valores}\033[m')
print(f'Os numeros Pares sao: \033[1;35m{par}\033[m')
print(f'Os numeros Impares sao: \033[1;36m{impar}\033[m')