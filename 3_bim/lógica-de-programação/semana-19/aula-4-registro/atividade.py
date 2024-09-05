x = int(input("Digite a orde do número de casos: "))

sequencia = []

for i in range(1, x+1):
    sequencia.extend([i] * i)
    print(f"Caso: {i}: {sequencia}")