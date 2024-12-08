import random

def criar_tabuleiro():
    """Cria um tabuleiro 3x3 com o tesouro escondido em uma célula aleatória."""
    grid = [[0 for _ in range(3)] for _ in range(3)]
    tesouro_x, tesouro_y = random.randint(0, 2), random.randint(0, 2)
    grid[tesouro_x][tesouro_y] = 1  # Coloca o tesouro
    return grid

def imprimir_tabuleiro(grid, mostrar_tesouro=False):
    """Imprime o tabuleiro, ocultando ou revelando o tesouro."""
    for linha in grid:
        print(' '.join('X' if celula == 1 and not mostrar_tesouro else 'T' if celula == -1 else '0' for celula in linha))

def jogar():
    grid = criar_tabuleiro()
    tentativas = 0
    print("Bem-vindo ao jogo 'Encontre o Tesouro'!")
    
    while True:
        imprimir_tabuleiro(grid)
        try:
            x = int(input("Escolha uma linha (0-2): "))
            y = int(input("Escolha uma coluna (0-2): "))
            
            if x < 0 or x > 2 or y < 0 or y > 2:
                print("Posição inválida. Escolha números entre 0 e 2.")
                continue
            
            if grid[x][y] == 1:
                tentativas += 1
                print(f"Parabéns! Você encontrou o tesouro em {tentativas} tentativa(s)!")
                imprimir_tabuleiro(grid, mostrar_tesouro=True)
                break
            elif grid[x][y] == -1:
                print("Você já tentou aqui. Tente outra posição.")
            else:
                print("Nada aqui. Continue procurando!")
                grid[x][y] = -1  # Marca a tentativa
                tentativas += 1
        except ValueError:
            print("Entrada inválida. Por favor, insira números inteiros.")
