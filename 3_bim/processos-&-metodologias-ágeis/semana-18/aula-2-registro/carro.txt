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

novo_carro = Carro("Polishop", "PSÉ", "2077", "Purple", "207.700")
novo_carro.imprimir()

# Alterações
novo_carro = Carro("Toyota", "Ching Chong", "2088", "White and Red", "500.000")
novo_carro.imprimir()
