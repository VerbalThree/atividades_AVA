# Pergunta ao usuário qual número ele quer multiplicar
user_num = int(input("Digite um número para multiplicar:\n"))

# Váriavel para ser o resultado final da multiplicação
result = 0

# Inicia um "for loop" para fazer a multiplicação, com uma range de 1 a 11
for i in range(1, 11):

    # Faz com que a váriavel "result" tenha o resultado da multiplicação e armazena elas
    result = user_num * i

    # Mostra a tabela de multiplicação
    print(f"{user_num} * {i}: {result}") 