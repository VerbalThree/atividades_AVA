class Livro:
    def __init__(self,titulo,autor,ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

        @property
        def titulo(self):
            return self.titulo
        
        @property
        def autor(self):
            return self.autor
        
        @property
        def ano(self):
            return self.ano
        
        @property
        def livros(self):
            return self.titulo
            return self.autor
            return self.ano
        
        def listar_livros(self):
            for livro in self.livros:
                print(f"{livro.titulo}, {livro.autor}, {livro.ano}")
                
        
        def adicionar_livro(self, livro):
            self.livros.append(livro)

