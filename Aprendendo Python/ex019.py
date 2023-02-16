import random
n1 = str(input('Digite o nome do primeiro aluno: '))
n2 = str(input('Digite o nome do segundo aluno: '))
n3 = str(input('Digite o nome do terceiro aluno: '))
n4 = str(input('Digite o nome do quarto aluno: '))
lista = [n1,n2,n3,n4]
escolhido = random.choice(lista)
print(escolhido)

import random
lista = []
for nome in range(4):
    nome = str(input("Digite um nome: "))
    lista.append(nome)
escolhido = random.choice(lista)
print(escolhido)

#for i in range(len(lista)):
#    print(lista[i])