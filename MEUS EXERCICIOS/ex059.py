from time import sleep

valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('[ 1 ] Somar\n'
      '[ 2 ] Multiplicar\n'
      '[ 3 ] Maior\n'
      '[ 4 ] Novos numeros\n'
      '[ 5 ] Sair\n')
    opcao = int(input('Qual a sua opcao: '))
    if opcao == 1:
        print(f'A soma entre {valor1} + {valor2} e igual a: {valor1 + valor2}')
        print('-=-'* 20)
        sleep(2)
    elif opcao == 2:
        print(f'A multiplicacao entre os numeros {valor1} e {valor2} e igual a: {valor1 * valor2}')
        print('-=-'* 20)
        sleep(2)
    elif opcao == 3:
        if valor1 > valor2:
            print(f'O numero {valor1} e maior que o numero {valor2}')
        elif valor2 > valor1:
            print(f'O numero {valor2} e maior que o {valor1}')
        else:
            print(f'Nao tem numero maior que o outro pois os dois sao iguais!')
    elif opcao== 4:
        print('Escolha os novos numeros')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    else:
        if opcao > 5 or opcao > 0:
            print(f'Opcao invalida!\nEscolha um dos numeros da lista!')
            print('-=-'* 20)
print('Programa Finalizado!')



