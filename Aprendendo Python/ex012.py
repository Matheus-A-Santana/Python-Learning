value = float(input('Qual é o preço do produto: R$'))
print('O produto custava R${}, na promoção com desconto de 5% vai custar {:.2f}'.format(value, value-(value*0.05)))