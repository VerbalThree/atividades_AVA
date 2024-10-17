import numpy as np

vendas = np.array([120, 130, 140, 150, 160, 170, 160, 150, 140, 130, 120, 110])

total_vendas = vendas.sum()
media_vendas = vendas.mean()
mes_maxima_venda = vendas.argmax() + 1 # Adicionando 1 para corresponder ao número do mês real

print("Total de vendas no ano: ", total_vendas)
print("Média mensal de vendas: ", media_vendas)
print("Mês com a máxima venda: ", mes_maxima_venda)