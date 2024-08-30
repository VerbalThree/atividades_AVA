import pandas as pd

# Exemplo de dataset (você pode carregar o seu dataset real)
filmes = pd.DataFrame({
    'titulo': ['Toy Story', 'Get Shorty', 'Ace Ventura', 'GoldenEye', 
               'The American President', 'Sabrina', 'Jumanji', 
               'Harry Potter and the Philosopher\'s Stone', 
               'The NeverEnding Story', 'The Chronicles of Narnia', 
               'The Golden Compass', 'The Indian in the Cupboard'],
    'generos': ['Animation|Children|Comedy', 'Comedy|Crime', 'Comedy', 
                'Action|Adventure|Thriller', 'Comedy|Drama|Romance', 
                'Comedy|Drama|Romance', 'Adventure|Children|Fantasy', 
                'Adventure|Children|Fantasy', 'Adventure|Children|Fantasy', 
                'Adventure|Children|Fantasy', 'Adventure|Children|Fantasy', 
                'Adventure|Children|Fantasy'],
    'total_de_votos': [50000, 30000, 40000, 45000, 32000, 29000, 51000, 
                       80000, 60000, 70000, 55000, 20000],
    'nota_media': [8.3, 7.5, 7.0, 8.0, 7.8, 7.2, 7.9, 8.5, 8.2, 7.9, 7.3, 6.8]
})

# Lista de filmes que você já assistiu
eu_assisti = [1, 21, 19, 10, 11, 7, 2]  # IDs fictícios para os filmes assistidos
# Usando títulos diretamente
filmes_assistidos = filmes.loc[[0, 1, 2, 3, 4, 5, 6]]  # Filmes assistidos

# Último filme assistido (exemplo: Jumanji)
ultimo_filme = filmes_assistidos.iloc[-1]
generos_ultimo_filme = ultimo_filme['generos']

# Recomendando filmes com base nos gêneros do último filme assistido
filmes_recomendados = filmes.query(f"generos == '{generos_ultimo_filme}'")

# Filtrando por filmes com mais de 50.000 votos e ordenando pela nota média
filmes_recomendados = filmes_recomendados[filmes_recomendados['total_de_votos'] > 50000]
filmes_recomendados = filmes_recomendados.sort_values(by='nota_media', ascending=False)

# Removendo filmes que você já assistiu
filmes_recomendados = filmes_recomendados[~filmes_recomendados['titulo'].isin(filmes_assistidos['titulo'])]

# Exibindo os filmes recomendados
print("Filmes recomendados para alguém que assistiu Jumanji:")
print(filmes_recomendados[['titulo', 'nota_media']].head(5))
