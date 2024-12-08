def lista_compras():
    lista = []  # Lista vazia para armazenar itens

    while True:
        print("\nOpções: ")
        print("1 - Adicionar item")
        print("2 - Remover item")
        print("3 - Exibir lista")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            item = input("Digite o item a ser adicionado: ")
            lista.append(item)
            print(f"'{item}' foi adicionado à lista.")
        elif opcao == '2':
            item = input("Digite o item a ser removido: ")
            if item in lista:
                lista.remove(item)
                print(f"'{item}' foi removido da lista.")
            else:
                print(f"'{item}' não encontrado na lista.")
        elif opcao == '3':
            print("\nLista de Compras:")
            for item in lista:
                print(f"- {item}")
        elif opcao == '4':
            print("Saindo do aplicativo.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
lista_compras()
