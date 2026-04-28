la=int(input('Qual a largura da parede? '))
al=int(input('Qual a altura da parede? '))
h=la*al
t=h/2 # cada lata cobre 2m
print('Sua parede tem {} metros quadrados'.format(h))
print('Voce precisa de {} latas de tinta para pintar a parede'.format(t))