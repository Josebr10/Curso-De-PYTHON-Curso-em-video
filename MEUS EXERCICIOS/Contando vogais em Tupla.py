palavras = ['APRENDER','PROGRAMAR','LINGUAGEM','PYTHON','CURSO','GRATIS',
            'ESTUDAR','PRATICAR','TRABALHAR','MERCADO','PROGRAMADOR','FUTURO','MILIONARIO ']
for letras in palavras:
    print(f'\nNa palavra {letras} temos: ',end=' ')
    for letra in letras:
        if letra.upper() in 'AEIOU':
            print(letra,end=' ')

