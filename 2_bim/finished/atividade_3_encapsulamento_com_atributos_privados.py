# Criação da Classe Termometro
class Termometro:
    def __init__(self, temperatura = 0): # Definindo a temperatura
        self._temperatura_celsius = temperatura # Definindo a temperatura em Celsius
        self._temperatura_fahrenheit = 0 # Definindo a temperatura em Fahrenheit

    @property # Definindo a temperatura em Celsius (Método Get)
    def temperatura_celsius(self):
        return self._temperatura_celsius 

    @property # Definindo a temperatura em Farenheit (Método Get)
    def temperatura_fahrenheit(self):
        return(self._temperatura_celsius * 9/5) + 32
    
    def definir_fahrenheit(self, temperatura_farenheit): # Definindo o método "definir_fahrenheit"
        self._temperatura_celsius = (temperatura_farenheit - 32) * 5/9

temp = Termometro() # Definindo a classe
temp.definir_fahrenheit(72) # Definindo a temperatura
print(temp.temperatura_fahrenheit) # Mostrando a temperatura