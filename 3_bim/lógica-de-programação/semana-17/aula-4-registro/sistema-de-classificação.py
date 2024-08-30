# Pede ao usuário colocar o valor do pedido
valor_pedido = int(input("Digite o valor do pedido: "))

# Pede ao usuário colocar os dias para a entrega 
dias_para_entrega = int(input("Digite os dias para entrega: "))

# Urgernte 

if valor_pedido > 500 or dias_para_entrega < 4:
    print("Pedido classificado como Urgente.")

# Normal

elif valor_pedido < 100 or dias_para_entrega > 7:
    print("Pedido classificado como Normal.")

# Prioritário

elif valor_pedido >= 100 or valor_pedido <= 500 and dias_para_entrega <= 7 or dias_para_entrega == 4:
    print("Pedido classificado como Prioritário")