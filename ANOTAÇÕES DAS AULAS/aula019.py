dados = dict() # cria um dicionario tambem
dados1 = { 'nome':'Jose', 'idade':20}
print(dados1['nome'])
print (dados1['idade'])
print (f'O seu nome e {dados1["nome"]} e a vc tem {dados1["idade"]} anos ')


# Para adicionar novos elementos em um dicionario

dados1['sexo']= 'M'

#REMOVER ELEMENTOS
del dados1['idade']
print(dados1)

#DICIONARIO GRANDE
filme = {'titulo':'Star Wars',
         'ano':'1977',
         'diretor':'George Lucas'
         }
print(filme.values()) # ELE PEGA OS ELEMENTOS DO DICIONARIO! "STAR WARS" , "1977" , "GEORGE LUCAS"


print(filme.keys()) #ELE VAI PEGAR AS VARIAVEIS DO DICIONARIO! "TITULO", "ANO", "DIRETOR"

print(filme.items()) # ELE VAI PEGAR AS VARIAVEIS E OS ELEMENTOS DO DICIONARIO!: ["TITULO""STAR WARS"] ["ANO""1977"],["DIRETOR""GEORGE LUCAS"]

for k, v in filme.items(): #FUNCIONA COMO UM ENUMERATE
    print(f'O {k} e {v}')


