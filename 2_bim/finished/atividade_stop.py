frutas_e_animais = ["Abacaxi", "Banana", "Cachorro", "Damasco", "Elefante", "Fuji", "Galinha", "Hortelã", "Iguana", "Jabuticaba", "Kiwi", "Leão", "Macaco", "Nectarina", "Onça", "Panda", "Quati", "Romã", "Sapoti", "Tangerina", "Uva", "Vaca", "Wampi", "Xixá", "Yuzu", "Zebra"]

letra = input("Digite a letra:\n").upper()

for fruta in frutas_e_animais:
    if fruta.startswith(letra):
        print(fruta)
