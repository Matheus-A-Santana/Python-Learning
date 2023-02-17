import random

def guess(x):
    randon_number = random.randint(1, x)
    guess = 0
    while guess != randon_number:
        guess = int(input(f'Adivinhe um número entre 1 e {x} '))
        if(guess < randon_number):
            print('desculpe, adivinhe novamente, muito baixo')
        elif guess > randon_number:
            print('desculpe, adivinhe novamente, muito alto')

    print(f'Parabéns você adivinhou o número. {randon_number}')

guess(10)