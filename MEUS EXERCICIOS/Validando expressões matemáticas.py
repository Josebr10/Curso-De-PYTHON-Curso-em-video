expressao = str(input('Digite a expressao: '))
pilha = []
for simb in expressao:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

print('-='*30)
if len(pilha) == 0:
    print('\033[1;32mSUA EXPRESSAO E VALIDA!!\033[m')

else:
    print('\033[1;31mSUA EXPRESSAO E INVALIDA!!\033[m')