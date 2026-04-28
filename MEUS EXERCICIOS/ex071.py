print('=' * 40)
print ('        BANCO DO ZEUEL           ')
print('=' * 40)
valor = int(input('Qual valor voce quer sacar? '))
total = valor
cedulas = 50
total_de_cedulas = 0
while True:
    if total >= cedulas:
        total -= cedulas
        total_de_cedulas += 1
    else:
        if total_de_cedulas > 0:
            print(f'Total de {total_de_cedulas} cedulas de R$ {cedulas}')
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 5
        elif cedulas == 5:
            cedulas = 2
        elif cedulas == 2:
            cedulas = 1
        total_de_cedulas = 0
        if total == 0:
            break

print('-'*40)
print('Volte sempre ao Banco Do ZEUEL!\n TENHA UM BOM DIA!')

