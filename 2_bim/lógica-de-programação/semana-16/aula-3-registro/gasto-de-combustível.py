# Pergunta ao usuário quanto tempo foi gasto na viagem e quanto foi a velocidade média
tempo_viagem = int(input("Quanto tempo foi gasto na viagem?\n"))
velocidade_media = int(input("Quanto foi a velocidade média? (em Km/h)"))

# Armazena quantos litros consome por Km
consumo_do_litro = 12

# Calcula a distância percorrida
distancia_percorrida = velocidade_media * tempo_viagem

# Calcula a quantidade de litros necessárias
litros_neccesários = distancia_percorrida / consumo_do_litro

# Exibe a quantidade de litros 
print(f"A quantidade de litros necessária é {litros_neccesários: 2f}")