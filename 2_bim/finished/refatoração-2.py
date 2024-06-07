# O uso incorreto do break estava na seguinte linha:

'''
numero = 1
while True:
    print(numero)
        numero += 1
    if numero > 10:
        break
--> break  <----

Quando o código terminava o "if numero > 10:" somente um break era necessário, não era necessário um segundo
'''

# A refatoração desse código é simplesmente mudando todo o laço while que existia para um laço for de 1 a 11
for i in range(1,11):

    # O código exibe cada um dos números
    print(f"{i}")