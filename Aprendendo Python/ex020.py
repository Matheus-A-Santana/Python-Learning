import random
lista = []
for nome in range(4):
    nome = str(input("Digite um nome: "))
    lista.append(nome)
print(lista)
random.shuffle(lista)
print("Ordem de apresentação: \n",lista)
