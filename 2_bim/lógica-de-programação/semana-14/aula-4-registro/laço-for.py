# Criação de uma lista de dicionários
livros = [
    {"titulo": "Meditações", "autor": "Marco Aurélio", "ano": "1909"},
    {"titulo": "Divina Comédia", "autor": "Dante Alighieri", "ano": "1321"}
]

# Criação de um laço for para iterar sobre o dicionário
for livro in livros:
    for chave, valor in livro.items(): # Chave: O identificador para acessar um valor específico \\\ Valor: O dado associado a chave
        print(f"{chave}: {valor}")
    print() # Uma linha branca entre os livros