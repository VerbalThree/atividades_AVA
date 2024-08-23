# Pede ao usuário para digitar quantas pessoas entraram no terceiro link
terceiro_link = int(input("Digite o número de usuários que entraram no terceiro link: "))

# Calcula quantas pessoas entraram no segundo link
segundo = terceiro_link * 2

# Calcula quantas pessoas entraram no primeiro link
primeiro = segundo + segundo

# Imprime quantas pessoas entraram em cada link
print(f"Primeiro link: {primeiro}\nSegundo link: {segundo}\nTerceiro link: {terceiro_link}")