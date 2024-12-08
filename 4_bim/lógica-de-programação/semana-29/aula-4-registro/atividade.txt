def gerenciar_inventario():
    inventario = {}  # Dicionário vazio para armazenar produtos e preços

    while True:
        print("\nOpções: ")
        print("1 - Adicionar produto")
        print("2 - Remover produto")
        print("3 - Exibir inventário")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            produto = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço do produto: "))
            inventario[produto] = preco
            print(f"'{produto}' foi adicionado ao inventário com o preço R${preco:.2f}.")
        elif opcao == '2':
            produto = input("Digite o nome do produto a ser removido: ")
            if produto in inventario:
                del inventario[produto]
                print(f"'{produto}' foi removido do inventário.")
            else:
                print(f"Produto '{produto}' não encontrado no inventário.")
        elif opcao == '3':
            print("\nInventário completo:")
            if inventario:
                for produto, preco in inventario.items():
                    print(f"{produto}: R${preco:.2f}")
            else:
                print("O inventário está vazio.")
        elif opcao == '4':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
gerenciar_inventario()
