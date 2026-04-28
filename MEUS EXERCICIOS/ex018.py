import math
import random
angulo=random.randint(1,360)
seno=math.sin(math.radians(angulo))
cosseno=math.cos(math.radians(angulo))
tangente=math.tan(math.radians(angulo))
print(f"O angulo sorteado foi o {angulo}:")
print(f'O Seno do numero {angulo} e igual a {seno:.2f} ')
print(f'O Cosseno do numero {angulo} e igual a {cosseno:.2f}')
print (f'A tangente do numero {angulo} e igual a {tangente:.2f}')
