# Loop while para solicitar números até o usuário digitar um número negativo
while True:
    numero = int(input("Digite um número (número negativo para sair): "))
    
    # Se o número for negativo, encerra o loop
    if numero < 0:
        break
    
    # Pula a verificação se o número for menor que 2
    if numero < 2:
        print("Número inválido, pois deve ser maior ou igual a 2.")
        continue
    
    # Verifica se o número é primo
    primo = True
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break
    
    # Exibe o resultado
    if primo:
        print(f"O número {numero} é primo.")
    else:
        print(f"O número {numero} não é primo.")
