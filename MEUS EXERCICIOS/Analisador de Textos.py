nome= str(input ('Digite seu nome completo: '))
nomema=nome.upper()
nomemi=nome.lower()
sem_espacos=len(nome.replace(' ',''))
primeiro_nome=len(nome.split()[0])



print (f'O seu nome com todas as letras maiusculas e: {nomema}')
print (f'O seu nome com todas as letras minusculas e: {nomemi}')
print(f'A quantidade de letras do seu nome sem espacos e igual a: {sem_espacos}')
print(f'A quantidade de letras do seu primeiro nome e: {primeiro_nome}')
