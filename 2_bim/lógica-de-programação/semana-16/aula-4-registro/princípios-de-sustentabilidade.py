# Pede ao usuário para inserir a pontuação de sustentabilidade da empresa
sustentabilidade_pont = int(input("Qual é a pontuação de sustentabilidade de sua empresa?\n"))

# Classifica a sustentabilidade da empresa
if sustentabilidade_pont >= 80:
    sustentavel = True
    print("A sua empresa é sustentável.\n")
elif sustentabilidade_pont < 80:
    sustentavel = False
    print("A sua empresa não é sustentável.\n")
else:
    print("Entrada de dados de incorreta. Verifique seus dados e tente novamente.\n")
    sustentavel = None