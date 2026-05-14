#Programa para aprovacao de emprestimo bancario
casa = float(input('Valor da casa: R$ '))
salario = float(input('Salario do Comprador: R$ '))
anos = int(input('Quantos anos de Financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print (f'Para pagar uma casa de R$ {casa:.2f} em {anos} anos')
print (f'A prestacao sera de R$ {prestacao:.2f}')

if prestacao <= minimo:
       print('Emprestimo pode ser \033[1:32mCONCEDIDO\033[m')
else:
       print('Emprestimo \033[1:31m NEGADO! \033[m')