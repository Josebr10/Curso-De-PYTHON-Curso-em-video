#Programa de calculo de anos para o alistamento militar
from datetime import date
atual = date.today().year
ano = int(input('Qual ano voce nasceu? '))
idade = atual - ano

print(f'Quem nasceu em {ano} tem {idade} anos em {atual}')

if idade == 18:
    print ('Voce tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    quanto_falta = 18 - idade
    print(f'Ainda faltam \033[1:32m{quanto_falta} \033[m anos para o seu alistamento')
else:
    quanto_passou = idade - 18
    print(f'Eita... Era para voce se alistar a \033[1:31m {quanto_passou}\033[m anos atras')



