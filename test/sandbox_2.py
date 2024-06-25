def create_adder(x):
    def adder(y):
        return x+y
    return adder

add_15 = create_adder(15)
print(add_15(10))


class Contador:
    def __init(self):
        self._valor = 0
        
    def criar_adicionar(x):
        def adicionador(y):
            return x+y
        return adicionador