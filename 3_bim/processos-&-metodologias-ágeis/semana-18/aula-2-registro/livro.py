class Livros:
    def __init__(self, titulo, autor, ano_publicacao, preco):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano_publicacao = ano_publicacao
        self.__preco = preco

    # Métodos Get 

    def get_titulo(self):
        return self.__titulo
    
    def get_autor(self):
        return self.__autor
    
    def get_ano_publicacao(self):
        return self.__ano_publicacao
    
    def get_preco(self):
        return self.__preco
    
    # Métodos Set

    def set_titulo(self, novo_titulo):
        self.__titulo = novo_titulo

    def set_autor(self, novo_autor):
        self.__autor = novo_autor
    
    def set_ano_publicacao(self,novo_ano_publicacao):
        self.__ano_publicacao = novo_ano_publicacao

    def set_preco(self, novo_preco):
        self.__preco = novo_preco

    # Imprime os resultados

    def imprimir(self):
        print("Título: %s\nAutor: %s\nAno de Publicação: %s\nPreço: R$%s\n" % (self.__titulo, self.__autor, self.__ano_publicacao, self.__preco))


# Definindo o livro
meu_livro = Livros("Clean Code", "Uncle Bob", "2012", "213,90")

# Imprimindo os resultados
meu_livro.imprimir()

# Definindo um novo livro
meu_livro = Livros("Meditações - Edição com Postais", "Marco Aurélio", "2019", "27,76")
meu_livro.imprimir()