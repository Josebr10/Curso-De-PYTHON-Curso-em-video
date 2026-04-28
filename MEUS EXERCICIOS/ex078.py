numeros = []
maior = 0
menor = 0
for c in range(0,5):
    numeros.append(int(input(f'Digite um valor para a posicao {c}: ')))
print('-='*30)
print(f'Os valores adicionados foram: {numeros}')
maior = max(numeros)
menor = min(numeros)

print(f'O maior valor foi o numero {maior} na posicao {numeros.index(maior)}  ')
print(f'O menor valor foi o numero {menor} na posicao {numeros.index(menor)}  ')

