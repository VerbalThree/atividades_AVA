temperaturas = [
    [22,25,28,32],
    [20,23,26,30],
    [18,22,25,29]
]

# Transposição da matriz
matriz_transposta = list(zip(*temperaturas))

print("Matriz transposta:")
for linha in matriz_transposta:
    print(linha)