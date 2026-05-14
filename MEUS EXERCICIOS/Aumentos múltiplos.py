from time import sleep

salario = float(input('Qual e o salario do funcionario? '))
print('PROCESSANDO...')
sleep(2)
if salario <= 1250:
   novo = salario + (salario * 15 / 100) #se fosse desconto seria: novo = salario - (salario * 15 / 100)
   print (f'O novo salario de quem recebe R${salario:.2f} e igual: R${novo:.2f} ')
else:
    novo = salario + (salario * 10 / 100)
    print (f'O salario de quem recebe R${salario:.2f} e igual: R${novo:.2f}')

