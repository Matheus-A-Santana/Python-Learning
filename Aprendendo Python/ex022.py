nome = str(input("Digite seu nome: ")).strip()
print("Analisando....")
print("seu nome maiusculo é: {}".format(nome.upper()))
print("seu nome em minusculo é: {}".format(nome.lower()))
print("seu nome tem ao todo {} letras".format(len(nome)-nome.count(' ')))
print("seu primeiro nome tem {} letras".format(nome.find(' ')))
