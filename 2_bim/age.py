age = int(input("Digite sua idade:\n"))

if age <= 12:
    categoria = "Criança"
    print("Você é: ", categoria)
elif age <= 17:
    categoria = "Adolescente"
    print("Você é: ", categoria)
elif age <= 64:
    categoria = "Adulto"
    print("Você é: ",categoria)
else:
    categoria = "Idoso"
    print("Você é: ", categoria)