# Armazena números de 1 a 5 para multiplicação
nums_1 = [1,2,3,4,5]

# Váriavel while para a primeira multiplicação
nums_while = False

# Armazena números de 1 a 10 para mult
nums_2 = [1,2,3,4,5,6,7,8,9,10]

# Váriavel while para a segunda multiplicação
nums_while_2 = False

# Começo do primeiro laço while para a primeira multiplicação
while not nums_while:

    # Laço for para fazer a multiplicação com todos os números
    for i in range(1,11):

        # Váriavel para armazenar o resultado das multiplicações
        result_1 = [i * x for x in nums_1]

        # Exibe os resultados
        print(result_1,"\n")

    # Define nums_while_2 para true e termina o segundo laço while    
    nums_while = True
    print("Fim da Primeira Multiplicação\n")

    # Aninhamento do segundo laço while
    while not nums_while_2:

        # Laço for para fazer a multiplicação com todos os números
        for i in range(1,11):

            # Váriavel para armazenar o resultado das multiplicações
            result_2 = [i * x for x in nums_2]

            # Exibe os resultados
            print(result_2,"\n")
        
        # Define nums_while_2 para true e termina o segundo laço while
        nums_while_2 = True
        print("Fim da Segunda Multiplicação\n")