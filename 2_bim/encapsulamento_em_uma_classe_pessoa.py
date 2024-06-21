class Pessoa:
    def __init__(self,nome,idade):
        self._nome = nome
        self._idade = idade

    @property # método get
    def nome(self):
        return self._nome
    
    @property # método get
    def idade(self):
        return self._idade
    
    @nome.setter # método set
    def nome(self, a):
        self._nome = a

    @idade.setter # método set
    def idade(self, b):
        self._idade = b