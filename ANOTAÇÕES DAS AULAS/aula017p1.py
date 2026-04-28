a = [2, 3, 4 , 7]
b = a[:] #FAZ COM QUE B RECEBA TODOS OS ELEMNTOS DE A, MAS NAO VAI ALTERA A QND FOR EDITAR OU REMOVER ALGO
b[2]= 8
print(f'A lista A: {a}')
print(f'A lista B: {b}')