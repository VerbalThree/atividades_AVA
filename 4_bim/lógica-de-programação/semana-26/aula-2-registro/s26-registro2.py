def main():
    import sys
    input = sys.stdin.read
    print("Digite todos os dados de entrada e finalize com CTRL-D (Unix) ou CTRL-Z (Windows) em uma nova linha:")
    data = input().split()
   
    if len(data) < 146:  # 1 linha + 1 operação + 144 valores
        print("Dados de entrada insuficientes.")
        return
   
    linha = int(data[0])  # Lê o índice da linha
    operacao = data[1]    # Lê a operação 'S' ou 'M'
    valores = list(map(float, data[2:146]))  # Lê os valores da matriz e os converte para float
 
    # Transformar a lista de valores em uma matriz 12x12
    matriz = [valores[i * 12:(i + 1) * 12] for i in range(12)]
   
    # Processar a matriz e obter o resultado
    resultado = processar_matriz(linha, operacao, matriz)
   
    # Imprimir o resultado
    print(resultado)
 
if __name__ == "__main__":
    main()