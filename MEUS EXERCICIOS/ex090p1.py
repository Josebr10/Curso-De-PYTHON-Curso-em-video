aluno = dict()
aluno['nome'] = str(input('Digite o nome do Aluno: '))
aluno['media'] = float(input(f'Qual a media do aluno {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao']= "\033[1;32mAPROVADO\033[m"
elif aluno['media'] >= 5:
    aluno['situacao'] = '\033[1;33mRECUPERACAO\033[m'
else:
    aluno['situacao'] = '\033[1;31mREPROVADO\033[m'

print('-='*30)
for k, v in aluno.items():
    print(f' - {k} e igual a {v}')