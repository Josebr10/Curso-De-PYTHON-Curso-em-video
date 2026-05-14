cont = soma = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Voce digitou \033[1;32m{cont}\033[m numeros\nA soma deles e igual a \033[1;32m{soma}\033[m')
