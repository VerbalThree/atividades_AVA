# Matriz de temperatura para 3 cidades ao longo de 4 meses
temperaturas = [
    [30,25,27,28],
    [22,24,26,23],
    [20,21,19,22]
]

def transpor_matriz(matriz):
    # Inicializa a matriz transposta com o número de colunas da matriz original (meses)
    linhas = len(matriz)
    colunas = len(matriz[0])

    # Cria uma matriz vazia com o número de linhas igual ao número de colunas da matriz original.
    matriz_transposta = [[0] * linhas for _ in range(colunas)]

    # Preencha a matriz transposta com os valores apropriados
    for i in range(linhas): # Percorre cada linha da matriz original
        for j in range(colunas): # Percorre cada coluna da matriz original
            matriz_transposta[j][i] = matriz[i][j] # Inverte a posição linha/coluna
    
    return matriz_transposta

# Transpondo a matriz
matriz_transposta = transpor_matriz_sem(temperaturas)

# Exibindo os dados
print("Matriz  Transposta (Linahs = Meses, Colunas = Cidades):")
for i, linha in enumerate(matriz_transposta):
    print(f"Mês {i + 1}: {linha}")