cont = soma = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Voce digitou {cont} numeros\nA soma deles e igual a {soma}')
print('FIM')