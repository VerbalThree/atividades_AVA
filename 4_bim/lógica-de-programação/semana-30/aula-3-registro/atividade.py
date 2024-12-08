def calcular_pedido():
    # Preços dos pratos
    precos = {
        "entrada": 20,
        "prato principal": 50,
        "sobremesa": 15
    }

    # Solicita ao usuário a quantidade e o tipo de prato
    tipo_prato = input("Digite o tipo de prato (entrada, prato principal, sobremesa): ").lower()
    quantidade = int(input(f"Digite a quantidade de {tipo_prato}(s): "))

    # Verifica se o tipo de prato é válido
    if tipo_prato in precos:
        total = precos[tipo_prato] * quantidade
    else:
        print("Tipo de prato inválido!")
        return

    # Aplica desconto se o total for maior que R$ 100
    if total > 100:
        total -= total * 0.10  # Desconto de 10%

    # Exibe o total com ou sem desconto
    print(f"O total do pedido é: R$ {total:.2f}")

# Executa o programa
calcular_pedido()
