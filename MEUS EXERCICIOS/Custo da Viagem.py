distancia = float(input('Qual a distancia da Viagem? '))
gasolina =0.50
gasolina_com_promocao = 0.45

print(f'Voce esta prestes a comecar a sua viagem de {distancia} KM.')
if distancia <= 200:
    print (f'O preco da Sua Passagem sera de R${distancia * gasolina:.2f}')
else:
    print(f'O preco da Sua Passagem sera de R${distancia * gasolina_com_promocao:.2f}')
