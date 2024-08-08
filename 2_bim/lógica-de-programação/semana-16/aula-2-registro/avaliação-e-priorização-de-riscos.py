# Pergunta qual é o nível de severidade e a probabilidade do risco
severidade = int(input("Qual é o nível de severidade? (1 a 5)\n"))
probabilidade = int(input("Qual é a probabilidade do risco? (1 a 5)\n"))

# Calcula a priorização dos riscos
if severidade > 3 and probabilidade > 3:
    print("Risco de alta prioridade.")
elif severidade > 3 or probabilidade > 3:
    print("Risco de média prioridade.")
else:
    print("Risco de baixa prioridade.")