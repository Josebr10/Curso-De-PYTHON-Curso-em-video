lanche = ('Hamburguer','Suco','Pizza','Pudim')
print(len(lanche)) # ISSO E PARA gLER QUANTOS ELEMENTOS TEM NA VARIAVEL
#Tuplas sao imutaveis
for contador in range(0, len(lanche)):  #METODO PARA LER COM RANGE
    print(lanche[contador])
print(lanche[:3])
for comida in lanche:      # FAZ A MESMA COISA DO RANGE, MAS E DIFERENTE
    print(f'Eu vou comer {comida}')

for pos,comida in enumerate(lanche):      # FAZ A MESMA COISA DO RANGE, MAS E DIFERENTE
    print(f'Eu vou comer {comida} na posicao {pos}')
print('Estava muito Gostoso!')

lanche = ('Hamburguer','Suco','Pizza','Pudim')
print(sorted(lanche)) # DEIXA EM ORDEM ALFABETICA

a = (2, 5, 4)
b = (5, 8, 2, 1)
c = a + b
print(a)
print(b)
print(c)
print(len(c)) # mostra quantos elementos tem na tupla
print(c.count(5)) # conta quantos 5 tem na tupla
print(c.index(8)) # mostra onde ta a posicao do numero escolhido na variavel

pessoa = ('Gustavo',39, 'M' ,99.88)
del(pessoa) #apaga da memoria uma tupla\E A UNICA COISA Q SE PODE FAZER NA TUPLA POR ELA SER IMUTAVEL
print(pessoa)
