# Criação do Objeto Contador
class Contador:
    def __init__(self):
        self._valor = 0     # Criação para definir o valor
        self._add = 1        # Criação para incrementar 1
        self._sub = 1       # Criação para diminuir 1

    @property  # Definição de valor (método get)
    def valor(self):
        print("Método Get")
        return self._valor

    @valor.setter # Definindo um um valor para "_valor" (Método Set) 
    def valor(self, a):
        self._valor = a
        
    @property # Definição de Add (método get)
    def add(self):
        return self._add
    
    @add.setter # Definindo um um valor para "_add" (Método Set)
    def add(self, a):
        self._add = a

    @property # Definição da Subtração (método get)
    def sub(self):
        return self._sub
    
    @sub.setter # Definindo um um valor para "_sub" (Método Set)
    def sub(self, a):
        self._sub = a

    def incrementar_1(self): # Criando a incrementação 
        self._valor += self._add
     
    def diminuir_1(self): # Criando a subtração
        self._valor -= self._sub
    
# Definindo a classe
contar = Contador()

contar.incrementar_1() # Incrementando 1
contar.incrementar_1() # Incrementando 1
contar.diminuir_1() # Subtraindo 1

print(contar.valor) # Mostrando o resultado