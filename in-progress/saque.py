# Pede para o usuario digitar o valor do saque
user_saque = int(input("Digite o valor do saque: "))

# Variavel para definir as notas
notas = [50,20,10,5]

# Variavel para definir a quantidade de notas
quantidade_notas = {}

# Laço for para escolher a quantidade de notas dentro das notas
for nota in notas:

    # Caso o valor do saque seja maior ou igual...
    if user_saque >= nota:

        # Define a quantidade de notas dentro da variavel "quantidade_notas"
        quantidade_notas[nota] = user_saque // nota

        # Arredonda o valor do saque
        user_saque = user_saque % nota

# Caso o usuario digite um valor menor que 5...
if user_saque != 0:

    # Exibe que não foi possivel encotrar as notas
    print("Não foi possível encotrar as notas para o seu saque desejado.\n")

# Mas caso seja possivel...
else:

    # Define a nota e quantidade com os itens da varialvel "quantidade_notas"
    for nota, quantidade in quantidade_notas.items():

        # E exibe a nota e a quantidade
        print(f"Nota: {nota}\nQuantidade: {quantidade}\n")
