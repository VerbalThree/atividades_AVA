# Perguntando quantos quilometros foram percorridos

valor_inteiro_x = float(input("Digite a distância total percorrida em Km: "))

# Perguntando quanto de combustível foi gasto

valor_real_y = float(input("Digite o total de combustível gasto: "))

# Calculo do consumo médio

consumo_medio = valor_inteiro_x / valor_real_y

# Exibindo o consumo médio

print(f"O consumo médio foi: {consumo_medio:.3f} km/l\n")
