dias_no_ano = 365
dias_no_mês = 30

# Pergunta para o usuário quantos dias ele já viveu
dias_vividos = int(input("Quantos dias você já viveu?"))

# Função para calcular a idade em anos e meses
def calc_idade(dias, dias_no_mês, dias_no_ano):
    anos = dias // dias_no_ano # Calcula os anos completos
    dias_restantes = dias % dias_no_ano # Calcula os dias restantes depois dos anos 
    meses = dias_restantes // dias_no_mês # Calcula os meses completos
    days_left = dias_restantes % dias_no_mês # Calcula os dias restantes depois dos meses

    return anos, meses, days_left

# Calcula a idade 
anos, meses, days_left = calc_idade(dias_vividos, dias_no_mês, dias_no_ano)

# Exibe os resultados
print(f"Você viveu por {anos} anos, {meses} meses e {days_left} dias.")