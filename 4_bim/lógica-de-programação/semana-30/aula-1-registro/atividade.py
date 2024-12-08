def avaliar_desempenho():
    # Solicita a pontuação de desempenho e a porcentagem de presença
    desempenho = float(input("Digite a pontuação de desempenho (0 a 100): "))
    presenca = float(input("Digite a porcentagem de presença (0 a 100): "))

    # Verifica a categoria do funcionário
    if desempenho >= 80 and presenca >= 90:
        categoria = "Excelente"
    elif 50 <= desempenho <= 79 and presenca >= 75:
        categoria = "Bom"
    elif desempenho < 50:
        categoria = "Ruim"
    else:
        categoria = "Regular"

    # Exibe a categoria
    print(f"A categoria do funcionário é: {categoria}")

# Executa o programa
avaliar_desempenho()
