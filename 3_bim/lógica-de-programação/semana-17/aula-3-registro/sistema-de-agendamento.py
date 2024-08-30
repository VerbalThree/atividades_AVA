def reuniao(participante, tipo_reuniao):

    # Verifica qual sala é adequada
    if participante > 15 or tipo_reuniao == "executiva":
        return "Sala Grande"
    elif participante <= 5:
        return "Sala Pequena"
    elif participante <= 15:
        return "Sala Média"
    
# Exemplo de uso
participante = int(input("Número de participante: "))

tipo_reuniao = input("Tipo de reunião: ").strip().lower()

if participante < 0:
    print("Não é possível realizar uma reunião sem participantes.")
elif tipo_reuniao not in ["normal", "executiva"]:
    print("Este tipo de reunião não existe.")
else:
    sala_recomendada = reuniao(participante, tipo_reuniao)
    print(f"A sala recomendada é {sala_recomendada}")