# Gerar lista de números pares de 0 a 20 usando compreensão de lista
numeros_pares = [num for num in range(21) if num % 2 == 0]

# Calcular o quadrado de cada número par usando compreensão de lista
quadrados = [num**2 for num in numeros_pares]

# Exibir as duas listas
print("Números pares:", numeros_pares)
print("Quadrados dos números pares:", quadrados)
