import random

print("Bem-vindo ao jogo de adivinhação em Python!\n")

numero_maximo = 51
numero_aleatorio = random.randint(1, numero_maximo)
quantidade_tentativas = 1

print(f"Digite um número entre 1 e {numero_maximo - 1} \n")

chute = input("Digite o número desejado: ")
chute_convertido = int(chute)

while (chute_convertido != numero_aleatorio):

    if chute_convertido < numero_aleatorio:
        print("O número secreto é maior!")
    else :
        print("O número secreto é menor!")

    chute = input("Digite o número desejado: ")
    chute_convertido = int(chute)
    quantidade_tentativas += 1
        
print(f"Parabéns, você acertou o número secreto com {quantidade_tentativas} tentativas.")
