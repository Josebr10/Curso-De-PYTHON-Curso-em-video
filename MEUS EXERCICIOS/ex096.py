def area():
    print('-' * 30)
    print('Controle de Terrenos')
    print('-' * 30)
    largura = float(input('Largura: '))
    comprimento = float(input('Comprimento: '))
    resultado = largura * comprimento
    print(f'A area do seu Terreno de {largura} x {comprimento} e de: {resultado} m²')


area()