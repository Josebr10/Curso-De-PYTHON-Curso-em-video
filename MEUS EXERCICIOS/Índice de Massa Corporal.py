peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura ** 2)

print (f'O seu IMC e igual a {imc:.2f}')
if imc < 18.5:
    print(f'Voce esta ABAIXO do peso')
elif imc <= 25:
    print(f'Voce esta no Peso IDEAL ')
elif imc < 30:
    print('Voce esta em SOBREPESO ')
elif imc < 40:
    print('Voce esta em OBESIDADE ')
else:
    print ('Voce esta em OBESIDADE MORBIDA')