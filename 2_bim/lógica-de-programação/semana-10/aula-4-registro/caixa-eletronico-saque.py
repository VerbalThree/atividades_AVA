# O código pede ao usuário para digitar o valor do saque
saque = int(input("Digite o valor do saque:"))

# O código define quais notas que existem
notas = [50,20,10,5]

# Variável para definir as quantidades de notas depois no for loop...
quantidade_notas = {}

# Um laço for para uma nota nas notas que existem
for nota in notas:

    # Caso o valor do saque seja igual ou maior que a nota...
    if saque >= nota:

        # O código define a quantidade de notas fazendo uma divisão por inteiro do saque pelas notas
        quantidade_notas[nota] = saque // nota

        # O código reduz o valor do saque para as notas calculadas
        saque = saque % nota

# O código verifica se é possível fazer o saque...
if saque != 0:

    # Caso não seja possível, o código informa ao usuário
    print("Não foi possível encontrar o valor das notas. Faça o saque com um número divisivel por 5.\n")

# Caso seja possível fazer o saque...
else:
    
    # O código inicia um laço for com as notas e quantidade nos itens das quantidades de notas
    for nota, quantidade in quantidade_notas.items():

        # O código informa o valor das notas e a quantidade de cada uma
        print(f"Valor da nota: {nota}\nQuantidade: {quantidade}")