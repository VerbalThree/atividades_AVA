# Diferente do código anterior, este código tem um laço for entre 1500 e 2700
for i in range(1500, 2700):

    # Quando é encontrado um número que é divisivel por 5 e 7...
    if(i % 5 == 0 and i % 7 == 0):

        # O código informa o número que foi encontrado
        print(f"O primeiro número divisível por 5 e 7 entre 1500 e 2700 é: {i}")
        
        # E termina o laço for
        break