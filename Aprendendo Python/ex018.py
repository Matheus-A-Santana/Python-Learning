import math
an = float(input('Digite o angulo que voce deseja: '))
seno = math.sin(math.radians(an))
co = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print('O angulo de {}\nseno de {:.2f}\ncosseno de {:.2f}\ntangente de {:.2f}'.format(an, seno, co, tan))
