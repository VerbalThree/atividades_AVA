valor1, valor2, valor3, valor4, valor5 = map(int, input("Digite os 5 valores separados por espaço: ").split())

pares = 0
impares = 0
positivos = 0
negativos = 0
zero = 0 # O valor é literalmente zero

for valor in [valor1, valor2, valor3, valor4, valor5]:
    if valor % 2 == 0:
        pares += 1
    if valor > 0:
        positivos += 1
    if valor < 0:
        negativos += 1
    if valor % 2 != 0:
        impares += 1
    if valor == 0:
        zero += 1

print(f"Pares: {pares}\nImpares: {impares}\nPositivos: {positivos}\nNegativos: {negativos}\nZero: {zero}")