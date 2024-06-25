condition = True

def calculo():
    
    while True:
        try:
            numero = float(input("Digite um número:\n"))
            break
        except ValueError:
            print("Somente números são lidos. Digite um número.\n")

    if numero > 0:
        print("O número que você digitou é positivo.\n")
    elif numero == 0:
        print("O número que você digitou é zero.\n")
    else:
        print("O número que você digitou é negativo.\n")
    user_input = (input("Você gostaria de usar este programa novamente? (sim/nao)\n"))
    if user_input != "sim":
        print("Programa encerrado.\n")
    else:
        calculo()    

calculo()