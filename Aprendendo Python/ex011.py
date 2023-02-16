largura = float(input('Largura da Parede: '))
Altura = float(input('Altura da Parede: '))
print('Sua parede tem {} x {} e sua área é de {}m²'.format(largura, Altura,(largura*Altura)))
print('Para pintar sua parede, você precisa de {:.2f}L de tinta'.format((largura*Altura)/2))