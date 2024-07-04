# O programa importa uma biblioteca para verificar os caracteres especiais
import re

# Armazena todos os caracteres especiais para verificar depois
especiais = re.compile('[@_/!#$%&*()<>?|}{~:]\ ')

# Pede ao usuário uma senha, podendo a senha ter números e letras
senha = input("Digite sua senha:\n")

# Verifica se a senha tem pelo menos 8 caracteres
while(len(senha) < 8) or (especiais.search(senha) != None):

    # Caso a senha não tenha 8 caracteres, o programa fala que não tem e pede ao usuário para fazer uma senha com 8 caracteres
    print("Desculpe, mas a sua senha não atende aos requisitos. É necessário ela ter pelo menos 8 caracteres.\n")

    # Pede ao usuário para fazer uma senha com 8 caracteres
    senha = input("Digite sua senha\n")
    
    # Quando o usuário faz uma senha que atende os requisitos, o programa fala que a senha foi definida com sucesso e mostra ela.
print(f"Senha definida com sucesso. A sua senha é: {senha}\n")

