#organizacao de categorias

from datetime import date

ano = int(input('Qual ano o seu atleta nasceu ? '))
idade = date.today().year - ano


if idade <= 9:
  print (f'Voce tem {idade} anos e esta dentro da categoria: \033[1:32m MIRIM\033[m')
elif idade <= 14:
    print (f'Voce tem {idade} anos e esta dentro da categoria: \033[1:33mINFANTIL\033[m')
elif idade <= 19:
    print (f'Voce tem {idade} anos e esta dentro da categoria: \033[1:34m JUNIOR\033[m')
elif idade <=25:
    print (f'Voce tem {idade} anos e esta dentro da categoria: \033[1:35m SENIOR\033[m')
else:
    print (f'Voce tem {idade} anos e esta dentro da categoria: \033[1:36m MASTER\033[m')