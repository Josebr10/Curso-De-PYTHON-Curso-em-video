
print ("-=-" * 30)
num = int(input('Digite um numero inteiro: '))
print ('''Escolha uma das bases para conversao:
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opcao: '))
if opcao == 1:
    print(f'{num} Convertido para numero binario e igual a: {bin(num)[2:]} ')
elif opcao == 2:
    print(f'{num} Convertido para OCTAL e igual a: {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} Convertido para numero HEXADECIMAL e igual a: {hex(num)[2:]} ')
else:
    print('\033[1:31m Opcao invalida! Tente novamente!\033[m')