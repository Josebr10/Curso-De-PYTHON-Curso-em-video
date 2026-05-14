print (str('=='*10),"Lojas ZEUEL",('=='*10))


preco = float(input('Digite o valor das compras: '))
print ('FORMA DE PAGAMENTO')
print ('''
[ 1 ] A VISTA DINHEIRO/CHEQUE
[ 2 ] A VISTA NO CARTAO
[ 3 ] 2X NO CARTAO
[ 4 ] 3X OU MAIS NO CARTAO''')

escolha = int(input('ESCOLHA UMA DAS OPCOES: '))

primeira_opcao = preco - (preco * 10/100)
segunda_opcao = preco - (preco * 5/100)
terceira_opcao = preco
quarta_opcao = preco + (preco * 20/100)

if escolha == 1:
    print (f' Voce escolheu \033[1:32m A VISTA DINHEIRO/CHEQUE \033[m\n'
           f' O valor final com base na sua escolha fica:\033[1:32m {primeira_opcao}\033[m\n')
elif escolha == 2:
    print (f' Voce escolheu \033[1:32m A VISTA NO CARTAO \033[m\n'
           f'O valor final com base na sua escolha fica: \033[1:32m{segunda_opcao}\033[m\n')
elif escolha == 3:
    print(f'Voce escolheu \033[1:32m 2X NO CARTAO \033[m\n'
          f'O seu gasto no inicio: {preco}'
          f'O valor final com base na sua escolha fica: 2 PARCELAS DE \033[1:32m{terceira_opcao / 2} \n PRECO FINAL: {terceira_opcao}\033[m\n')
elif escolha == 4:
    print(f'Voce escolheu \033[1:32m 3X OU MAIS NO CARTAO \033[m\n')
    parcela = int(input('Quantas parcelas? '))
    print (f' O valor final com base na sua escolha fica:\n {parcela} VEZES DE {preco / parcela:.2f} \n PRECO FINAL:\033[1:32m {quarta_opcao}\033[m')

