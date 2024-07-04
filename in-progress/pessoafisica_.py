from pessoa import Pessoa

class Pessoa_Fisica(Pessoa):
    def __init__(self, CPF, nome, idade):
        super().__init__(nome, idade) # O super serve para invocar os atributos da classe Pessoa
        self.CPF = CPF

    def getCPF(self):
        return self.CPF
    def setCPF(self, CPF):
        self.CPF = CPF