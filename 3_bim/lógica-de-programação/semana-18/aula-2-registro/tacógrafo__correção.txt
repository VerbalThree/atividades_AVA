def calcular_distancia(t,v):
    if 1 <= t <= 100 and 0 <= v <= 120:
        return t * v
    elif t == 0 and v == 0:
        return 0
    else:
        return -1
    
# Leitura dos intervalos
T1, V1 = map(int, input("Digite o tempo e a velocidade para o intervalo 1 (separado por espaço): ").split())
T2, V2 = map(int, input("Digite o tempo e a velocidade para o intervalo 2 (separado por espaço): ").split())
T3, V3 = map(int, input("Digite o tempo e a velocidade para o intervalo 3 (separado por espaço): ").split())

# Calculo das distancias para cada intervalo
distancia1 = calcular_distancia(T1,V1)
distancia2 = calcular_distancia(T2,V2)
distancia3 = calcular_distancia(T3,V3)

# Verificação de entradas invalidas 
if distancia1 == -1 or distancia2 == -1 or distancia3 == -1:
    print("Entrada Inválida.")
else:
    distancia_total = distancia1 + distancia2 + distancia3
    print(f"Distância total percorrida: {distancia_total}")