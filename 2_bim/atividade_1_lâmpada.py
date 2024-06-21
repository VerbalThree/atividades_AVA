class Lampada:
    def __init__(self, desligada=False):
        self._ligada = not desligada
        self._estado = self.ligada

    @property # Defindo "Ligada" (Métod get)
    def ligada(self):
        return self._ligada

    @property # Defindo "Desligada" (Métod get)
    def desligada(self):
        return not self._ligada
    
    @property # Defindo "Estado" (Métod get)
    def estado(self):
        return self._estado
    
    def ligar(self):
        if self._ligada == False:
            self._ligada = True
            self._estado = self._ligada
            print("A lâmpada está ligada.")
        else:
            print("A lampada já está ligada.")

    def desligar(self):
        if self._ligada == True:
            self._ligada = False
            self._estado = self._ligada
            print("A lâmpada está desligada.")
        else:
            print("A lâmpada já está desligada.")

    def alterar_estado(self):
        if self.ligada == True:
            self.desligar()
            print("Estado alterado para desligado.")
        else:
            self.ligar()
            print("Estado alterado para ligado.")

lamp = Lampada()
print(lamp.alterar_estado())
print(lamp.alterar_estado())
