valores = []
for c in range(0,5):
    n = int(input("Digite um Valor: "))
    if c == 0 or n > valores[-1] : #SIMPLIFICANDO CONDICOES
        valores.append(n)
        print('ADICIONADO AO FINAL DA LISTA')
    else:
        pos = 0
        while pos < len(valores):
            if n<= valores[pos]:
                valores.insert(pos,n)
                print(f'ADICICIONADO NA POSICAO {pos} DA LISTA')
                break
            pos += 1
print('-='*30)
print(f'Os valores digitador em ordem foram {valores}')