valor = int(input("Digite um valor: "))
valores = [valor]

# Preenche o vetor com o dobro do valor anterior
for i in range(1,10):
    valores.append(valores[i-1]*2)

# Mostra os valores
for i in range(10):
    print(f"N[{i}] = {valores[i]}")