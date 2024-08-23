def calcular(competidores, qnt_folhas, qnt_folhas_especiais):
    if qnt_folhas_especiais % competidores == 0:
        return "SIM".upper()
    else:
        return "NAO".upper()



competidores, qnt_folhas, qnt_folhas_especiais = map(int, input("Digite a quantidade de competidores, o número de folhas que cada competidor deve receber e a quantidade de folhas especiais compradas: ").split())

possibilidade = calcular(competidores, qnt_folhas, qnt_folhas_especiais)
print(possibilidade)

# 100 especiais 
# 33 players
# é suficiente se: cada competidor tem direito a 3 folhas de papel