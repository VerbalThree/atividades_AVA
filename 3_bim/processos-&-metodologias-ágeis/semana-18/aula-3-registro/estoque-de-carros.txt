class Carro:
    def __init__(self, marca,modelo,ano,cor,preço):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
        self.__cor = cor
        self.__preço = preço
    
    # Métodos Get

    def get_marca(self):
        return self.__marca
    
    def get_modelo(self):
         return self.__modelo

    def get_ano(self):
         return self.__ano
    
    def get_cor(self):
         return self.__cor
    
    def get_preço(self):
         return self.__preço

    # Métodos Set

    def set_marca(self,nova_marca):
         self.__marca = nova_marca
    
    def set_modelo(self,novo_modelo):
         self.__modelo = novo_modelo
         
    def set_ano(self,novo_ano):
         self.__ano = novo_ano

    def set_cor(self,nova_cor):
         self.__cor = nova_cor
        
    def set_preço(self,novo_preço):
         self.__preço = novo_preço

    # Imprimir os resultados

    def imprimir(self):
         print("Novo marca: %s\nNovo Modelo: %s\nNovo Ano: %s\nNova Cor: %s\nNovo preço: R$%s\n" % (self.__marca,self.__modelo,self.__ano,self.__cor,self.__preço))

class Estoque:
    def __init__(self):
        self.__carros = [] # lista de carros vazia
        
    def adicionar_carro(self,Carro):
         self.__carros.append(Carro)
         print(f"Carro {Carro.get_marca()} {Carro.get_modelo()} adicionado.\n")

    def remover_carro(self,Carro):
         if Carro in self.__carros:
              self.__carros.remove(Carro)
              print(f"O carro {Carro.get_marca()} {Carro.get_modelo()} foi removido")
         else:
              print("Carro não encontrado")

    def listar_carros(self):
         for i in self.__carros:
              print(f"Marca: {i.get_marca()}\nModelo: {i.get_modelo()}\n")

carro1 = Carro("Honda", "Civic", "2012", "Preto", "100,000")
carro2 = Carro("Ferrari", "Performance", "2011", "Vermelho", "200,000")

carro1.imprimir()
carro2.imprimir()

estoque = Estoque()
estoque.adicionar_carro(carro1)
estoque.adicionar_carro(carro2)
estoque.listar_carros()
estoque.remover_carro(carro1)