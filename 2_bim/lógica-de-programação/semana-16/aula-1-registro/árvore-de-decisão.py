sintoma_febre = input("O paciente tem febre? (sim/não) ").strip().lower()

# Converte a resposta para uma boolean
if sintoma_febre and sintoma_febre[0] == 's':
    febre = True
elif sintoma_febre and sintoma_febre[0] == 'n':
    febre = False
else:
    print("Resposta inválida. Responda com 'sim' ou 'não'. ")
    febre = None

sintoma_tosse = input("O paciente tem tosse? (sim/não) ").strip().lower()

# Converte a resposta para uma boolean
if sintoma_tosse and sintoma_tosse[0] == 's':
    tosse = True
elif sintoma_tosse and sintoma_tosse[0] == 'n':
    tosse = False
else:
    print("Resposta inválida. Responda com 'sim' ou 'não'. ")
    tosse = None

# Verifica os sintomas e faz o diagnóstico
if febre == True and tosse == True:
    print("Possível diagnóstico: Gripe")
elif febre == True and tosse == False:
    print("Possível diagnóstico: Infecção viral")
else:
    print("Sintomas não específicos, consulte um médico.")