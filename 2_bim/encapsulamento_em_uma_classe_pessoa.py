class Pessoa:
    def __init__(self,nome,idade):
        self.__nome = nome
        self.__idade = idade

    @property # método get
    def nome(self):
        return self.__nome
    
    @property # método get
    def idade(self):
        return self.__idade
    
pessoas = Pessoa("Rafael", 33)
print(pessoas.nome)
print(pessoas.idade)