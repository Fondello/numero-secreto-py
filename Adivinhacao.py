import random

print("Bem-vindo ao jogo de adivinhação em Python!\n")

numero_maximo = 50
numero_aleatorio = random.randint(1, numero_maximo)
quantidade_tentativas = 1

print("Digite um número entre 1 e {} \n".format(numero_maximo))

chute = input("Digite o número desejado: ")
chute_convertido = int(chute)

while chute_convertido != numero_aleatorio:

    if chute_convertido < numero_aleatorio:
        print("O número secreto é maior!")
    else:
        print("O número secreto é menor!")

    chute = input("Digite o número desejado: ")
    chute_convertido = int(chute)
    quantidade_tentativas += 1

print("Parabéns, você acertou o número secreto com {} tentativas.".format(quantidade_tentativas))
