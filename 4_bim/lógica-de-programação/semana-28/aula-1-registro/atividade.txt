def move_left(grid):
    def compress(row):
        return [num for num in row if num != 0] + [0] * (len(row) - len([num for num in row if num != 0]))

    def merge(row):
        for i in range(len(row) - 1):
            if row[i] != 0 and row[i] == row[i + 1]:
                row[i] *= 2
                row[i + 1] = 0
        return row

    new_grid = []
    for row in grid:
        compressed = compress(row)
        merged = merge(compressed)
        new_row = compress(merged)
        new_grid.append(new_row)
    
    return new_grid

# Exemplo de teste:
matriz = [
    [2, 2, 0, 2],
    [4, 0, 4, 4],
    [0, 0, 2, 2],
    [2, 0, 0, 2]
]
resultado = move_left(matriz)
for linha in resultado:
    print(linha)
