import random

# Define o número secreto

num_secreto = random.randint(1, 100)

# Verifica se o usuario acertou

tentativas = 0
adivinha = False

# Pede um número ao usuario

while not adivinha:
    palpite = int(input("Digite um número entre 1 e 100\n"))
    tentativas += 1

# Verificar se o palpitel é maior ou menor que o num_secreto

    if palpite < num_secreto:
        print("O número secreto é maior.\n")
    elif palpite > num_secreto:
        print("O número secreto é menor\n")
    else:
        print("Você acertou o número secreto em ", tentativas, " tentativas\n")
        adivinha = True