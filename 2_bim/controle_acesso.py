class Usuario:
    def __init__(self,nome,senha):
        self._nome = nome
        self._senha = senha

    # GETTERS

    @property
    def nome(self):
        return self._nome
    
    @property
    def senha(self):
        return self._senha
    
    # SETTERS

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @senha.setter
    def senha(self, senha):
        self._senha = senha

    def new_psw(self, new_psw):
        self._senha = new_psw

user = Usuario("Jão", "newpsw123")
print(user.nome, user.senha)
user.new_psw("newpsw456")
print(user.nome, user.senha)
