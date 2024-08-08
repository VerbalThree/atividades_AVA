# Pergunta para o usuário qual é o tipo de risco
tipo_de_risco = input("Qual é o tipo de risco: Operacional, Financeiro ou Mercado?").strip().lower()

# Verifica qual é o tipo de risco
if tipo_de_risco and tipo_de_risco[0] == 'o':
    tipo_operacional = True
    print("O seu tipo de risco é Operacional.")
elif tipo_de_risco and tipo_de_risco[0] == 'f':
    tipo_financeiro = True
    print("O seu tipo de risco é Financeiro.")
elif tipo_de_risco and tipo_de_risco[0] == 'm':
    tipo_mercado = True
    print("O seu tipo de risco é Mercado.")
else:
    print("Nenhum tipo de risco detectado. Verifique a sua entrada.")