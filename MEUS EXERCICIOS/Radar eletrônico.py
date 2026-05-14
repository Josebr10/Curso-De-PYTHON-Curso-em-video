velocidade = float(input('Qual e a velocidade Atual do seu Carro? '))
multa = 7 * (velocidade - 80)
if velocidade <= 80:
  print('Tenha um Bom dia! Dirija com seguranca!')
else:
    print(f'MULTADO!! Voce excedeu o limite permitido que e de 80 KM/h\n Voce deve pagar uma multa de R$ {multa} ')