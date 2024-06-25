custo = float(input("Quanto foi o total?\n"))
desconto = 10.0

if custo > 100:
    preco = (custo / desconto) 
    total = custo - preco
    print("Você obteve 10% de desconto, logo, o preço total será: R$", total)
else:
    total = custo
    print("Você não obteve desconto. Logo, o preço total é: R$", total)