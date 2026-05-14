soma = produto_caro = menor = barato = cont = 0
print('='*40)
print('            LOJA SUPER BARATAO             ')
print('='*40)
while True:
    nome_do_produto = str(input('Nome do produto: '))
    preco = float(input('Preco: R$ '))
    cont += 1
    soma += preco
    if preco > 1000:
        produto_caro += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome_do_produto


    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print('-'*20,'\033[1;32mFIM DO PROGRAMA\033[m','-'*20)
print(f'O total da compra foi \033[1;32mR${soma:.2f}\033[m')
print(f'Temos {produto_caro} produto custando mais de R$ 1000')
print(f'O produto Mais barato foi {barato} que custa R$ {menor:.2f}')
print('Acabou')







