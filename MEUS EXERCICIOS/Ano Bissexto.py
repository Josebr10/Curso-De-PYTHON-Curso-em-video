from datetime import date

ano = int(input('Que ano que analisar? '))
bissexto = ano % 4
if ano == 0:
    ano = date.today().year
if bissexto == 0:
    print(f'O ano de {ano} foi BISSEXTO! ')
else:
    print(f'O ano de {ano} nao foi BISSEXTO! ')

