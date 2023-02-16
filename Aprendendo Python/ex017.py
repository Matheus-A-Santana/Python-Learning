import math
catOpos = float(input('Digite o Cateto oposto: '))
catAdj = float(input('Digite o Cateto Adjacente: '))
#Hipote = ((catOpos **2) + (catAdj ** 2)) ** 0.5
#print('A hipotenusa irá medir: {:.2f}'.format(Hipote))
print('A hipotenusa irá medir: {:.2f}'.format(math.hypot(catOpos, catAdj)))