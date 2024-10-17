temperaturas = [
    [18, 19, 20, 21, 22, 23, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3],
    [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44],
]

# Lista para armazenar os dias com média superior a 20°C
dias_com_media_superior = []

# Itera sobre cada dia (linha da matriz)
for dia in range(len(temperaturas)):
    media = sum(temperaturas[dia]) / len(temperaturas[dia]) # Calcula a média da linha (dia)

    if media > 20:
        dias_com_media_superior.append(dia + 1) # Adiciona o dia à lista (somando 1 para ajuste de índice)
    print(f"Dia {dia + 1}: Média de {media:.2f}°C")

# Exibe os dias em que a temperatura média foi superiro a 20°C
if dias_com_media_superior:
    print(f"Os dias com temperatura média superir a 20°C são: {dias_com_media_superior}")
else:
    print("Nenhum dia teve temperatura média superior a 20°C")