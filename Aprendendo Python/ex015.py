dias = int(input('Quantos dias alugados: '))
km = float(input('Quanto km rodados: '))
print('O total a pagar é de R${:.2f}'.format((km * 0.15) + (dias * 60)))