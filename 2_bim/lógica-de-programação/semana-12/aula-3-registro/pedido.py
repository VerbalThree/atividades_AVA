pedido = int(input("Qual o valor do pedido?\n"))
taxa_fixa = 0
desconto_clube = 0

if pedido < 10:
    taxa_fixa = 5
    print(f"Taxa Fixa de {taxa_fixa} reais.")
elif pedido >= 10 and pedido < 20:
    taxa_fixa = 3
    print(f"Taxa Fixa de {taxa_fixa} reais.")
elif pedido >= 20:
    taxa_fixa = 0
    print(f"Taxa Fixa de {taxa_fixa} reais.")

membro_fidelidade = input("Você é membro do programa fidelidade?\n")

if membro_fidelidade == "Sim" or membro_fidelidade == "sim":
    desconto_clube = 2
    print(f"Desconto de {desconto_clube} reais do clube.\n")
if membro_fidelidade == "nao":
    desconto_clube = 0
    print("Sem desconto do clube.")

total_taxa = taxa_fixa - desconto_clube
if pedido == 0:
    print(f"Valor Total: Grátis\nTaxa de Entrega: {total_taxa}\n")
else:
    print(f"Valor Total: {pedido} reais.\nTaxa de Entrega: {total_taxa} reais.\n")