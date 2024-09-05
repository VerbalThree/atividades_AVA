n = int(input("Digite um valor: "))

v1 = 1
v2 = 1

for i in range(n*2):
    print(f"{v1} {v2} {v1**3 + (i%2)}")
    v1 += (i%2)
    v2 += (i+1)