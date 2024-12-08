import random

def criar_tabuleiro():
    """Cria um tabuleiro 3x3 com o tesouro em uma posição aleatória."""
    tabuleiro = [[0 for _ in range(3)] for _ in range(3)]
    x, y = random.randint(0, 2), random.randint(0, 2)
    tabuleiro[x][y] = 1
    return tabuleiro, (x, y)

def jogar():
    tabuleiro, pos_tesouro = criar_tabuleiro()
    print("Bem-vindo ao jogo 'Encontre o Tesouro'!")
    tentativas = 0

    while True:
        try:
            print("\nEscolha uma posição (linha e coluna entre 0 e 2):")
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))

            if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
                print("Posição inválida. Tente novamente.")
                continue

            tentativas += 1

            if tabuleiro[linha][coluna] == 1:
                print(f"Parabéns! Você encontrou o tesouro em {tentativas} tentativa(s)!")
                break
            else:
                print("Nada aqui. Continue procurando!")
        except ValueError:
            print("Entrada inválida. Insira números inteiros entre 0 e 2.")

jogar()
