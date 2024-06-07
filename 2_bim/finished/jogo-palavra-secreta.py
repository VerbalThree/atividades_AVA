# O programa importa a biblioteca random
import random

# O programa faz uma lista de palavras para escolher
palavras_secretas = ["computador", "geladeira", "porta"]

# O programa escolha uma dessas palavras
palavra_secreta = (random.choice(palavras_secretas))

# Variável para definir e armazenar o número de tentativas
tentativas = 0

# Variável para definir se o usuário acertou a palavra ou não
acertou = False

# Variável para definir se o usuário digitou somente uma letra
verificaçao = False

# Um loop while para verificar se o usuário digitou somente uma letra
while not verificaçao:

    # Pede ao usuário para digitar uma letra
    user_letra = input("Digite uma letra\n")
    
    # Caso o usuário não digitou somente uma letra, o programa pede ao usuário para digitar novamente uma letra.
    if len(user_letra) != 1:
        print("Você digitou mais do que uma letra. Digite novamente\n")
    
    # Verifica se o usuário digitou somente uma letra
    if len(user_letra) == 1:

        # Começa um while loop para o jogo
        while not acertou:

            # Verifica se a primeira letra do usuário não é igual ao da palavra secreta
            if user_letra != palavra_secreta[0]:
                
                # Incrementa mais um para as tentativas e armazena elas
                tentativas += 1

                # O programa pede para tentar novamente
                print("Tente novamente.\n")
                break
            
            # Verifica se o usuário acertou a primeira letra ou a palavra inteira 
            elif user_letra == palavra_secreta[0]:

                # Define a variável "acertou" para True e termina o while loop
                acertou = True

                # Define a variável "verificaçao" para True e termina o while loop
                verificaçao = True

                # Diz ao usuário que ele acertou a palavra
                print("Parabéns, você acertou a palavra secreta. A palavra secreta era ", palavra_secreta.capitalize())
        
        # Caso o usuário atingir u número máximo de tentativas...
        if tentativas == 3:

            # O programa exibe que o usuário perdeu...
            print("Você perdeu. A palavra secreta era: ", palavra_secreta.capitalize())
            
            # E define as variáveis "acertou" e "verificaçao" para True e termina todo o jogo e verificação
            acertou = True
            verificaçao = True



