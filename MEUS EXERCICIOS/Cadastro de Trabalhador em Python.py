from datetime import date

informacoes = dict()
informacoes['nome'] = str(input('Nome: '))
ano_nascimento = int(input('ano de nascimento: '))
informacoes['idade'] = date.today().year - ano_nascimento
informacoes['ctps'] = int(input('carteira de Tranalho (0 Nao tem): '))
if informacoes['ctps'] != 0:
    informacoes['contratacao']= int(input('Ano de contratacao: '))
    informacoes['salario']= float(input('Salario R$: '))
    informacoes['aposentadoria'] = informacoes['idade'] + (informacoes['contratacao'] + 35) - date.today().year
print('-='*30)

for k, v in informacoes.items():
    print(f' - {k} tem o valor {v}')
