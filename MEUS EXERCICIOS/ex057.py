sexo = str(input('Informe o seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('\033[1:31m Dados Invalidos!\033[m \n Por favor, Digite novamente: ')).strip().upper()[0]
print(f'\033[1:32m Sexo {sexo} Registrado com sucesso!')
