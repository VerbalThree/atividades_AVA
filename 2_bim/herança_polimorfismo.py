class Veiculo:
    def acelerar(self):
        raise NotImplementedError("Método acelerar deve ser implementado.")
    
class Carro(Veiculo):
    def acelerar(self):
        print("Carro acelerando.")

class Motocicleta(Veiculo):
    def acelerar(self):
        print("Motocicleta acelerando.")

        