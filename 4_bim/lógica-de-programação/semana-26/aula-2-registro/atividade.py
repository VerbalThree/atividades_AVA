linha_Da_Matriz = int(input("Digite o valor da linha da matriz: "))
while linha_Da_Matriz < 0 or linha_Da_Matriz > 11:
    print("Por favor, digite um valor entre 0 e 11.")
    linha_Da_Matriz = int(input("Digite o valor da linha da matriz: "))

caractere =  input("Digite o caractere: ").upper() 

while caractere != "M" and caractere != "S":
    print("Por favor, digite 'S' para soma ou 'M' para média")
    caractere =  input("Digite o caractere: ").upper() 

# Criação da matriz M[12][12] e leitura dos elementos
matriz = []
print("Digite os 144 valores da matriz (12 linhas x 12 colunas):")
for i in range(12):
    linha = []
    for j in range(12):
        valor = float(input(f"Elemento [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

# Realizando a operação na linha indicada
soma = sum(matriz[linha_Da_Matriz]) # Soma dos elementos da linha

# Exibir o resultado baseado na operação escolhida
if caractere == "S":
    print(f"Soma dos elementos da linha {linha_Da_Matriz}: {soma:.1f}")
elif caractere == "M":
    media = soma / 12
    print(f"Média dos elementos da linha {linha_Da_Matriz}: {media:.1f}")