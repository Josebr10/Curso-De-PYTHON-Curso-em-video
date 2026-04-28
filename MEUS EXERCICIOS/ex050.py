soma = 0
cont = 0
for c in range(1,7):
    num = int(input(f'Digite o {c} valor: '))
    if num % 2 == 0:
        soma += num
        cont += cont + 1
print(f'Voce informou \033[1:36m {cont}\033[m  numeros PARES e a soma deles e igual a \033[1:35m {soma} \033[m ')