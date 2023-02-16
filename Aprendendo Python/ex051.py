primeiro = int(input('Primeiro Termo: '))
razao = int(input('Termo: '))
decimo = primeiro + (10 - 1) * razao

for c in range(primeiro, decimo, razao):
    print('{}'.format(c), end=' -> ')
print('ACABOU')