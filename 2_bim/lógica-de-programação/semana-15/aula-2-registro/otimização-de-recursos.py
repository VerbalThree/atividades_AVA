# Criação de um dicionário
equipe = {
    "devs": 50,
    "designers": 20,
    "gerentes": 15,
    "orçamento": 1000000
}

# Criação de uma lista de dicionários para os projetos
projetos = [
    {"nome": "Projeto A", "devs-min": 15, "designers-min": 5, "gerentes-min": 3, "orçamento-min": 200000},
    {"nome": "Projeto B", "devs-min": 10, "designers-min": 8, "gerentes-min": 2, "orçamento-min": 250000},
    {"nome": "Projeto C", "devs-min": 5, "designers-min": 2, "gerentes-min": 1, "orçamento-min": 100000},
    {"nome": "Projeto D", "devs-min": 20, "designers-min": 4, "gerentes-min": 4, "orçamento-min": 300000},
    {"nome": "Projeto E", "devs-min": 8, "designers-min": 6, "gerentes-min": 2, "orçamento-min": 150000}
]

# Função para verificar a viaiblidade dos projetos
def verificar_viabilidade(equipe,projetos):
    devs_disponiveis = equipe["devs"]
    designers_disponiveis = equipe["designers"]
    gerentes_disponiveis = equipe["gerentes"]
    orçamento_disponivel = equipe["orçamento"]

    projetos_viaveis = []

    for projeto in projetos:
        devs_min = projeto["devs-min"]
        designers_min = projeto["designers-min"]
        gerentes_min = projeto["gerentes-min"]
        orçamento_min = projeto["orçamento-min"]

        # Verificar se a equipe atende aos requisitos
        equipe_atende = (
            devs_disponiveis >= devs_min and
            designers_disponiveis >= designers_min and
            gerentes_disponiveis >= gerentes_min
        )

        # Verificar se o orçamento disponível cobre o orçamento mínimo
        orçamento_suficiente = orçamento_disponivel >= orçamento_min

        if equipe_atende and orçamento_suficiente:
            projetos_viaveis.append(projeto["nome"])

    return projetos_viaveis

# Verifica quais projetos são viáveis
projetos_viáveis = verificar_viabilidade(equipe, projetos)
print("Projetos viáveis", projetos_viáveis)