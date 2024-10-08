nota1, nota2 = map(float, input("Digite as duas notas separado por espaço: ").split())

if nota1 < 0 or nota2 < 0:
    print("Nota inválida")
else:
    media = (nota1 + nota2) / 2
    print(media)