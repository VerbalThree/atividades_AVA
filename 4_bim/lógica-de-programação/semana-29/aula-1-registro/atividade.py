def calcular_preco():
    print("Bem-vindo à loja de roupas!")
    try:
        qtd_pecas = int(input("Digite a quantidade de peças compradas: "))
        preco_unitario = float(input("Digite o preço unitário das peças: "))

        # Determinação do desconto
        if qtd_pecas <= 5:
            desconto = 0
        elif 6 <= qtd_pecas <= 10:
            desconto = 0.10  # 10%
        else:
            desconto = 0.20  # 20%

        # Cálculo do preço total e preço com desconto
        preco_total = qtd_pecas * preco_unitario
        valor_desconto = preco_total * desconto
        preco_final = preco_total - valor_desconto

        # Exibição do resultado
        print("\nResumo da Compra:")
        print(f"Preço total: R${preco_total:.2f}")
        print(f"Desconto aplicado: {desconto * 100:.0f}% (R${valor_desconto:.2f})")
        print(f"Preço final: R${preco_final:.2f}")
    except ValueError:
        print("Entrada inválida. Por favor, insira valores numéricos válidos.")

# Executa o programa
calcular_preco()
