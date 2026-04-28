lado1 = int(input('Informe o primeiro lado do trinagulo: '))
lado2 = int(input('Informe o segundo lado do triangulo: '))
lado3=int(input('Informe o terceiro lado do triangulo: '))

if lado1 == lado2 == lado3:
    print("Voce formou um \033[1:36m TRIANGULO EQUILATERO!\033[m")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print('Voce formou um \033[1:32mTRIANGULO ISOSCEELES!\033[m')
else:
    print('Voce formou um \033[1:33mTRIANGULO ESCALENO!\033[m')
