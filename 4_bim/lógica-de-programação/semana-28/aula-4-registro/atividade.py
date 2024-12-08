import random

def criar_tabuleiro():
    """Gera um tabuleiro 3x3 com um único zero em posição aleatória."""
    tabuleiro = [[1 for _ in range(3)] for _ in range(3)]
    x, y = random.randint(0, 2), random.randint(0, 2)
    tabuleiro[x][y] = 0
    return tabuleiro, (x, y)

def imprimir_tabuleiro(tabuleiro):
    """Imprime o tabuleiro, ocultando o zero."""
    for linha in tabuleiro:
        print(' '.join('1' if celula == 0 else str(celula) for celula in linha))

def jogar():
    """Gerencia o fluxo do jogo."""
    tabuleiro, pos_zero = criar_tabuleiro()
    tentativas = 0
    print("Bem-vindo ao jogo 'Caça ao Zero'!")
    
    while True:
        imprimir_tabuleiro(tabuleiro)
        try:
            linha = int(input("Escolha uma linha (0-2): "))
            coluna = int(input("Escolha uma coluna (0-2): "))

            if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
                print("Posição inválida. Escolha números entre 0 e 2.")
                continue

            tentativas += 1

            if (linha, coluna) == pos_zero:
                print(f"Parabéns! Você encontrou o zero em {tentativas} tentativa(s)!")
                break
            else:
                print("Nada aqui. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira números inteiros.")
