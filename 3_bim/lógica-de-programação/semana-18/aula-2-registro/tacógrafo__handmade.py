'''
O código a seguir foi feito "na raça" tem o propósito de calcular a distância total de quantos intervalos o
usuário quiser.
'''

class tacografo:
    def __init__(self,tempo,velocidade,distancia_total):
        
        # Define o tempo, velocidade e distância total para o usuário colocar em cada intervalo
        self.tempo = tempo
        self.velocidade = velocidade
        self.distancia_total = distancia_total

def adicionar_intervalos(Intervalo, qnt_intervalos):

    # Caso o intervalo atual seja igual a quantidade de intervalos, o programa para de pedir os dados dos intervalos    
    if Intervalo == qnt_intervalos:
        return

    # Pede ao usuário colocar o total de tempo e a velocidade    
    tempo = int(input(f"Digite a quantidade de tempo do {Intervalo + 1}º intervalo: "))
    velocidade = int(input(f"Digite a velocidade do {Intervalo + 1} intervalo: "))
    
    # Calcula a distância total do intervalo atual
    distancia_total = tempo * velocidade 
    
    # Adiciona o intervalo
    intervalo = tacografo(tempo,velocidade,distancia_total)
    
    # Adiciona esse intervalo na lista de intervalos
    Intervalos.append(intervalo)

    # Adiciona mais 1 "Intervalo" para o usuário registrar
    adicionar_intervalos(Intervalo + 1, qnt_intervalos)

# Array para definir os intervalos  
Intervalos = []

# Intervalo presente 
Intervalo = 0

# Pede ao usuário para colocar a quantidade de intervalos
qnt_intervalos = int(input("Digite a quantidade de intervalos: "))

# Uso da função "adicionar_intervalos" para o usuário definir os dados de cada intervalo
adicionar_intervalos(0, qnt_intervalos) # (começa no 0 e vai até a quantidade de intervalos que o usuário colocou)

# Calcula o total percorrido e imprime o resultado
total_percorrido = sum(map(lambda intervalo: intervalo.distancia_total, Intervalos)) # Seleciona a distância total de todos os intervalos e soma eles

# Exibe o total
print(f"O total percorrido foi: {total_percorrido}")