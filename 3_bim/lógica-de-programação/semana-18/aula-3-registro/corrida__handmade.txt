def ponto_décimo(C,N):
    if 1 < C < 10**8 and 1 < N < 100:
        return N - C

# O programa pede ao usuário para colocar o valor dos metros e do comprimento da corrida
C, N = map(int, input("Digite a número de metros e o comprimento da pista respectivamente: ").split())

ponto_decimo = ponto_décimo(C,N)
print(f"O ponto décimo é {ponto_decimo}")