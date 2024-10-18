def vender(estoque, produto, quantidade):
    if estoque[produto-1] >= quantidade:
        estoque[produto-1] -= quantidade
    else:
        print("Estoque insuficiente")

def adicionar(estoque, produto, quantidade):
    estoque[produto-1] += quantidade

def exibir_estoque(estoque):
    for i, qtd in enumerate(estoque, start=1):
        print(f"Produto {i} ; {qtd}, unidades")

# Estoque inicial
estoque = [20, 15, 10, 30, 5]

# Operações
vender(estoque, 1, 3)
vender(estoque, 4, 2)
adicionar(estoque, 5, 10)
exibir_estoque(estoque)