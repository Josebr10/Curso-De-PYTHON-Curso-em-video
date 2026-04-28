aluno = {}
nota= {}
while True:
    aluno['nome']= str(input('Nome: '))
    nota['media']= float(input(f'Media de {aluno["nome"]}: '))
    for nome in aluno:
        print(f'Nome e igual a {aluno["nome"]}')
    for media in nota:
        print(f'Media e igual a {nota["media"]}')
        if nota["media"] >= 7:
            print('A situacao e \033[1;32mAPROVADO!\033[m')
        else:
            print('A situacao e \033[1;31mREPROVADO!\033[m')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'Nn':
        break
print('-='*30)
print('O PROGRAMA ACABOU!')