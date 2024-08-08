# Quantidade de figurinha dos jogadores
figurinhas_player_1 = 8
figurinhas_player_2 = 12

# Calcula o total de figurinhas
total_figurinhas = figurinhas_player_1 + figurinhas_player_2

# Calcula a quantidade ideal de figurinhas para cada jogador
quantidade_ideal = total_figurinhas / 2

# Calcula a quantidade que cada jogador precisa dar ou receber
def calc_quantidade_troca(figurinhas_1, figurinhas_2):
    ideal_1 = quantidade_ideal - figurinhas_1
    ideal_2 = quantidade_ideal - figurinhas_2

    # Se a quantidade ideal for positiva, o jogador precisa receber essas figurinhas, caso o contrário o jogaodr precisa dar essas figurinhas (nesse caso, o valor absoluto utilizando a função abs() )
    return abs(ideal_1), abs(ideal_2)

# Calcula as quantidades para trocar
quant_para_trocar = calc_quantidade_troca(figurinhas_player_1, figurinhas_player_2)

# Exibe a quantidade de figurinhas que precisa ser trocada 
print("Figurinhas para trocar entre os jogadores: ", quant_para_trocar )
