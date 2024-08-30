import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
df = pd.read_csv('movies.csv')
# Supondo que os gêneros estão separados por '|' na coluna 'genres'
df['genres'] = df['genres'].str.get_dummies(sep='|')
similarity_matrix = cosine_similarity(df.drop('title', axis=1))
def recommend_movie(movie_title, df, similarity_matrix):
    if movie_title not in df['title'].values:
        return "Filme não encontrado no dataset."
    
    # Pegando o índice do filme
    idx = df[df['title'] == movie_title].index[0]
    
    # Similaridade dos filmes
    similarity_scores = list(enumerate(similarity_matrix[idx]))
    
    # Ordenar os filmes por similaridade
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    
    # Pegar os 5 filmes mais similares
    similar_movies = [df['title'].iloc[i[0]] for i in similarity_scores[1:6]]
    
    return similar_movies
recommended_movies = recommend_movie('Toy Story', df, similarity_matrix)
print("Filmes recomendados:", recommended_movies)
