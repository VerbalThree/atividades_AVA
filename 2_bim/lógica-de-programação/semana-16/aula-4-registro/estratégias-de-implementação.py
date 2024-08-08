# Pede ao usuário para inserir o custo de implementação e o impacto esperado
implementação_custo = int(input("Quanto é o custo de implementação?\n"))
impacto_expectativa = int(input("Em uma faixa de 1 a 10, quanto é a expectativa do impacto?\n"))

# Calcula o custo de implementação e a expectativa do impacto e classifica a estratégia de implementação
if implementação_custo < 50000 and impacto_expectativa >= 7:
    viavel = True
    print("Classificado como viável.\n")
else:
    viavel = False
    print("Análise Adicional Necessária.\n")