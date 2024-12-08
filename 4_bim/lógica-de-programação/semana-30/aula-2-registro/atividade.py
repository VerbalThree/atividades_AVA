def recomendar_filme():
    # Solicita a idade e a preferência de gênero
    idade = int(input("Digite sua idade: "))
    genero = input("Digite sua preferência de gênero (ação, comédia, drama): ").lower()

    # Verifica as condições de recomendação
    if idade >= 18:
        if genero == "ação" or genero == "comédia":
            recomendacao = "Filme de ação ou comédia para adultos"
        elif genero == "drama":
            recomendacao = "Filme de drama para adultos"
        else:
            recomendacao = "Gênero inválido"
    else:
        if genero == "ação" or genero == "comédia":
            recomendacao = "Filme de ação ou comédia para adolescentes"
        elif genero == "drama":
            recomendacao = "Filme de drama para adolescentes"
        else:
            recomendacao = "Gênero inválido"
    
    # Exibe a recomendação de filme
    print(recomendacao)

# Executa o programa
recomendar_filme()
