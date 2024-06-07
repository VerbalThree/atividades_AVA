# O erro no código anterior estava no break duplicado

'''
O código correto é da seguinte maneira:

numero = 1
while True:
    print(numero)
    numero += 1
    if numero > 10:
        break
'''

# A minha refatoração:

for i in range(1,11):
    print(i)