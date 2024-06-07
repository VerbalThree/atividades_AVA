import random

# Seleciona um número aleatório de 1 a 50
num_aleatorio = random.randint(1, 50)

# Verifica se o usuário acertou
acertou = False

# Armazena as tentativas do usuário
tentativas = 0

while not acertou:

    # Pergunta ao usuário qual número ele acha ser
    user_adivinhacao = int(input("Digite o número que você acha ser:\n"))

    # Caso o número que o usuário digitou é menor que o número aleatório, o programa fala que o número aleatório é maior e adiciona mais uma tentativa para o usuário
    if user_adivinhacao < num_aleatorio:
        tentativas += 1
        print("O número secreto é maior.\n")

    # Caso o número que o usuário digitou é maior que o número aleatório, o programa fala que o número aleatório é menor e adiciona mais uma tentativa para o usuário
    elif user_adivinhacao > num_aleatorio:
        tentativas += 1
        print("O número secreto é menor.\n")
    else:

    # Caso o usuário acerte, o programa diz que o usuário acertou e mostra as tentativas
        print("Acertou!. Você tentou ", tentativas, " vezes.\n")

    # Define "acertou" para True e termina o jogo. 
        acertou = True

    # Caso o usuário atingir o número máximo de tentativas, o programa fala que o usuário perdeu e mostra qual era o número aleatório
    if tentativas == 5:
        print("Você perdeu. O número secreto era: ", num_aleatorio)
    
    # Termina o loop para acabar com o jogo
        break