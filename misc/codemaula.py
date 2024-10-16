def aula():
    letra = (input("Digite uma letra:\n"))
    letra = letra.lower()
            
    if letra == 'a':
        print("Abelha\n")
    elif letra == 'b':
        print("Bombom\n")
    elif letra == 'c':
        print("Cadeira")
    elif letra == 'd':
        print("Dado")
    elif letra == 'e':
        print("Eletricidade")
    elif letra == 'f':
        print("Faca\n")
    elif letra == 'g':
        print("Gus")
    elif letra == 'h':
        print("High")
    elif letra == 'i':
        print("Instância")
    elif letra == 'j':
        print("Janta")
    elif letra == 'u':
        print("Uva")
    elif letra == 'v':
        print("Verbal")
    elif letra == 'k':
        print("Kiwi")
    elif letra == 'l':
        print("Limão")
    elif letra == 'm':
        print("Mamão")
    elif letra == 'n':
        print("Nova")
    elif letra == 'o':
        print("Ouvido")
    elif letra == 'p':
        print("Print")
    elif letra == 'q':
        print("Queijo")
    elif letra == 'r':
        print("Resistence")
    elif letra == 's':
        print("Sunday")
    elif letra == 't':
        print("Televisão")
    elif letra == 'w':
        print("Window")
    elif letra == 'x':
        print("Xperia")
    elif letra == 'y':
        print("Yogurt")
    elif letra == 'z':
        print("Zebra")
    else:
        user_answer = (input("Nenhuma letra foi encontrada.\nVocê gostaria de usar este programa novamente? (sim/não)\n"))
        if user_answer == "sim":
            aula()
        else:
            print("Programa encerrado.\n")

aula()

