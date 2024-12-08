# Inicializa variáveis para soma e contagem
soma = 0
contador = 0

# Loop while para solicitar números até que o usuário digite 0
while True:
    numero = int(input("Digite um número (0 para finalizar): "))
    
    if numero == 0:
        break  # Encerra o loop quando o número é 0
    
    soma += numero  # Adiciona o número à soma
    contador += 1  # Incrementa a contagem de entradas

# Calcula e exibe a média
if contador > 0:
    media = soma / contador
    print(f'A média dos números digitados é: {media}')
else:
    print("Nenhum número válido foi digitado.")
