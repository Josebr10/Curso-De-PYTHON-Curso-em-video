n=int(input('Digite um numero qualquer de 0 a 9999: '))
unidade = n % 10
dezena = ( n // 10) % 10
centena = (n // 100) % 10
milhar = (n // 1000) % 10


print (f'UNIDADE:{unidade}')
print (f'DEZENA:{dezena}')
print (f'CENTENA:{centena}')
print (f'MILHAR:{milhar}')


#n = n.zfill(4)

#u= n[3]
#d = n[2]
#c= n[1]
#m= n[0]