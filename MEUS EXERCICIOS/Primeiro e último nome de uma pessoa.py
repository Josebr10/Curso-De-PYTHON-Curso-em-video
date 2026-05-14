nome= input(f'Digite seu nome: ').strip()

partes=nome.split()

fnome=partes[0]
lnome=partes[-1]

print(f'Seu primeiro nome e: {fnome}')
print(f'Seu ultimo nome e: {lnome}')