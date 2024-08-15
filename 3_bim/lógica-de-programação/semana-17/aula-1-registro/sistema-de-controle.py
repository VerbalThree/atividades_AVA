def sistema():
    print("Gerente: 1\nAnalista: 2\nEstagiário: 3\n")
    cargo = int(input("Digite o número do seu cargo: "))

    print("Segunda-Feira: 2\nSábado: 7\n")
    dia_da_semana = int(input("Digite o dia da semana: "))

    if cargo == 1:
        print("Você tem acesso irrestrito.\n")
    elif cargo == 3 and dia_da_semana in range(2,7):
        print("Você tem acesso somente aos dias úteis.\n")
    elif cargo == 2 and dia_da_semana in [7,1]:
        print("Você tem acesso somente aos finais de semana.\n")
    else:
        print("Cargo não encontrado.\n")

while True:
    sistema()
    reiniciar = input("Gostaria de 'reiniciar o programa? (S/N)\n").strip().lower()
    if reiniciar and reiniciar[0] != 's':
        print("Programa encerrado.\n")
        break
    else:
        sistema()
