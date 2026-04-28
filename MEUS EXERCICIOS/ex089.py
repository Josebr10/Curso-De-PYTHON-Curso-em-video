from time import sleep
ficha = list()

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media =(nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer Continuar? [S/N]')).upper().strip()[0]
    if resposta in 'Nn':
        break

print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*30)
    opc = int(input("Qual aluno voce quer ver as Notas? [999]INTERROMPE!"))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) -1:
        print('PROCESSANDO...')
        sleep(2)
        print(f'As Notas de {ficha[opc][0]} sao {ficha[opc][1]}')
    elif opc > len(ficha) -1:
        print('Aluno Nao Identificado! Por favor, Digite um aluno valido!')

sleep(2)
print('<<<< VOLTE SEMPRE >>>>')
