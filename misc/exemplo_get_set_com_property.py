class Contador:
    def __init__(self):
        self._valor = 0
    
    @property
    def valor(self):
        print("getter method called")
        return self._valor
    
    @valor.setter
    def valor(self, a):
        if(a < 18):
            raise ValueError("Sorry you age is below eligibility criteria")
        print("setter method called")
        self._valor = a

rej = Contador()
rej.valor = 12
print(rej.valor)










"""
contador = Contador()
print(contador.get_valor())
"""

class Contador:
    def __init(self):
        self._valor = 0
        
    def criar_adicionar(x):
        def adicionador(y):
            return x+y
        return adicionador