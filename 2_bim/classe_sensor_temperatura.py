class SensorTemperatura:
    def __init__(self, temperatura=0):
        self.__temperatura = temperatura

    def nova_temp(self, nova_temp): # definição de nova_temp
        if -50 <= nova_temp <= 150:
            self.__temperatura = nova_temp
        else:
            print("Temperatura fora do intervalo permitido.")

    @property # método get
    def temperatura(self):
        return self.__temperatura
    
sensor = SensorTemperatura()
sensor.nova_temp(25)
print(sensor.temperatura)