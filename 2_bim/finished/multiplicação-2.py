# Variável para definir o começo do primeiro laço while
primeira_multiplicação = False

# Variável para definir o começo do segundo laço while
segunda_multiplicação = False

# Array para os números da primeira multiplicação
nums_1 = [1,2,3,4,5]

# Array para os números da segunda multiplicação
nums_2 = [1,2,3,4,5,6,7,8,9,10]

# Começo do primeiro while e primeira multiplicação
while not primeira_multiplicação:
    
    # For loop para fazer a multiplicação dos números com um alcance de 1 a 11
    for i in range(1,11):

        # Variável para definir o resultado da primeira multiplicação
        result_1 = [i * x for x in nums_1]

        # Tabela das multiplicações
        print(result_1)

    # Variável definida como verdadeira para terminar o primeiro laço while   
    primeira_multiplicação = True

    # Indicando o fim do primeiro laço while
    print("Fim do Primeiro Laço While\n")

    # Começo do segundo laço while e segunda multiplicação
    while not segunda_multiplicação:

        # For loop para fazer a multiplicação dos números com um alcance de 1 a 11
        for j in range(1,11):

            # Variável para definir o resultado da segunda multiplicação
            result_2 = [j * x for x in nums_2]

            # Tabela das multiplicações
            print(result_2)

        # Variável definida como verdadeira para terminar o segundo laço while  
        segunda_multiplicação = True

        # Indicando o fim do segundo laço while
        print("Fim do Segundo Laço While\n")