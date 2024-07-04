class ContaBancaria:
    def __init__(self, saldo_inicial = 0):
        self.__saldo = saldo_inicial
        self.__saldo_adicionado = 0
    
    @property # método get
    def saldo(self):
        return self.__saldo

    @property #método get
    def saldo_adicionado(self):
        return self.__saldo_adicionado
    
    def adicionar_saldo(self, saldo_adicionado):
        self.__saldo += saldo_adicionado
        


rgj = ContaBancaria()
print(rgj.saldo)