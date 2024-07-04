class Livro:
    def __init__(self,titulo,autor,ano):
        self._titulo = titulo
        self._autor = autor
        self._ano = ano
        self.livros = []

        # GETTERS

    @property
    def titulo(self):
        return self._titulo
        
    @property
    def autor(self):
        return self._autor
        
    @property
    def ano(self):
        return self._ano
        
        # SETTERS

    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo

    @autor.setter
    def autor(self, autor):
        self._autor = autor

    @ano.setter
    def ano(self,ano):
        self._ano = ano

    def adicionar_livro(self, livro):
        self.livros.append(livro)   

    def listar_livro(self):
        for livro in self.livros: 
            print(f"{livro['titulo']}, {livro['autor']}, {livro['ano']}")        

bkl = Livro("Titulo", "Autor", 2023)
bkl.adicionar_livro({"titulo" : "1984", "autor": "George Orwell", "ano": 1949})
bkl.adicionar_livro({"titulo" : "I, Robot", "autor": "Isaac Asimov", "ano": 1950})
bkl.listar_livro()