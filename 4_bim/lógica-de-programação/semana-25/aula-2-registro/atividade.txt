def reservar_assentos(sala, fileira, assento):
    if sala[fileira-1][assento-1] == 0:
        sala[fileira-1][assento-1] = 1
    else:
        print("Assento já está reservado")

def cancelar_reserva(sala, fileira, assento):
    if sala[fileira-1][assento-1] == 1:
        sala[fileira-1][assento-1] = 0
    else:
        print("Este assento não está reservado")

def exibir_sala(sala):
    for fila in sala:
        print("".join(map(str, fila)))

# Mapa inicial
sala = [[0] * 8 for _ in range(5)]

# Operações
reservar_assentos(sala, 1,3)
reservar_assentos(sala, 2,5)
reservar_assentos(sala, 4,7)
cancelar_reserva(sala, 2,5)
exibir_sala(sala)