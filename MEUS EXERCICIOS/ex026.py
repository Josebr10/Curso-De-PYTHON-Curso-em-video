frase=input('Digite uma frase: ')
letra_a= frase.count('a')
posicao_a_inicial=frase.find('a')
posicao_a_final=frase.rfind('a')

print(f'Quantas vezes a letra a aparece nessa frase:{letra_a} ')
print(f'qual a posicao que a letra a aparece no inicio da frase:{posicao_a_inicial} ')
print(f'Qual a ultima posicao que a letra A aparece:{posicao_a_final} ')
