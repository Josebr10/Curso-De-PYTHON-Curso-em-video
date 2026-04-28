numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite outro numero; '))
if numero1 > numero2:
    print(f'O PRIMEIRO NUMERO: {numero1} e maior que o {numero2}')
elif numero2 > numero1:
    print(f'O SEGUNDO NUMERO: {numero2} e maior que o {numero1}')
else:
  print(f'Os numeros {numero1} e {numero2} sao iguais')
