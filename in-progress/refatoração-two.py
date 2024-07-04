# Laço for para números entre 1500 e 2700
for i in range(1500, 2700):

    # Caso o número é divisivel por 5 e 7...
    if(i % 5 == 0 and i % 7 == 0):
        # Exibe qual é o primeiro número divisivel por 5 e 7...
        print(f"O número divisivel por 5 e 7 é {i}")
        
        # E termina o laço for
        break