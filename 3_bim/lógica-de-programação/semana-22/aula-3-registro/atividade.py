# n = quantidade de casos 

n = int(input("Digite a quantidade de casos: "))

valores = []

for i in range(n):

    x1, y1 = map(int, input("Digite os números para descobrir a soma: ").split())
    valores.append((x1, y1))

soma_impares = 0

for x1, y1 in valores:
    if x1 % 2 != 0:
        soma_impares += x1
    if y1 % 2 != 0:
        soma_impares += y1 

print(f"A soma dos valores impares é {soma_impares}")