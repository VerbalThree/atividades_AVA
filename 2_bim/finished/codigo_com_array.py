def stop_jogo():

    frutas_e_animais = ["Abacaxi", "Banana", "Cachorro", "Damasco", "Elefante", "Fuji", "Galinha", "Hortelã", "Iguana", "Jabuticaba", "Kiwi", "Leão", "Macaco", "Nectarina", "Onça", "Panda", "Quati", "Romã", "Sapoti", "Tangerina", "Uva", "Vaca", "Wampi", "Xixá", "Yuzu", "Zebra"]

    letra = input("Digite a letra:\n").upper()

    for fruta in frutas_e_animais:
        if fruta.startswith(letra):
            print(fruta)

    user_answer = input("Você gostaria de usar este programa novamente?\n(sim/não)\n")
    if user_answer != "sim":
        print("Programa encerrado.\n")
    else:
        stop_jogo()

stop_jogo()
