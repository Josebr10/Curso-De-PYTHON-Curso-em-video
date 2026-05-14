resp = 'S'
quant = media = soma = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um numero: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > menor:
            maior = n
        elif n < maior:
            menor = n
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print (f'Voce digitou {quant} numeros e a media foi {media}')
print(f'O maior numero foi {maior} e o menor foi {menor}')
