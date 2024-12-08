def verificar_pontuacao():
    # Solicita ao usuário a pontuação final
    pontuacao = int(input("Digite sua pontuação final: "))

    # Usa operador ternário para determinar o resultado
    resultado = "Ganhou" if pontuacao >= 50 else "Perdeu"

    # Exibe o resultado
    print(f"Você {resultado}!")

# Executa o programa
verificar_pontuacao()
