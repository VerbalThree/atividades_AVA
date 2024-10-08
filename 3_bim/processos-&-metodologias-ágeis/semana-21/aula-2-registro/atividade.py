class ContaBancaria:
    def __init__(self,numero_conta,saldo = 0,numero_transaçoes = 0):
        self.numero_conta = numero_conta
        self.transações = []
        self.saldo = saldo
        self.numero_transaçoes = numero_transaçoes

    def consultar_saldo(self):
        print(f"Saldo: {self.saldo}")

    def depositar(self,valor):
        self.saldo += valor
        self.numero_transaçoes += 1
        self.registar_transaçoes("Depósito", valor)

    def sacar(self,valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.
            self.registar_transaçoes("Saque", valor)
        else:
            print("Saldo insuficiente")

    def registar_transaçoes(self,tipo,valor):
        self.transações.append({"Tipo":tipo,"Valor":valor})

    def historico_transaçoes(self):
        return self.transações
    
class ContaCorrente(ContaBancaria):
    def __init__(self,numero_conta,saldo=0):
        super().__init__(numero_conta,saldo)

class CalculadoraTarifas:
    @staticmethod
    def calcular_tarifa_base():
        return 5
    
    @staticmethod
    def calcular_tarifa_transaçao(tran)

contaCorrente = ContaCorrente("1")
contaCorrente.depositar(1000)
contaCorrente.sacar(250)
print(f"Transações: {contaCorrente.historico_transaçoes()}")
print(f"Número da conta: {contaCorrente.numero_conta}")
contaCorrente.consultar_saldo()