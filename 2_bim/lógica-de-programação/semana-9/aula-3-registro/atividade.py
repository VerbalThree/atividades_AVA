class elementos:
    def __init__(self, elemento, numero_atomico, nome, massa):
        self.elemento = elemento
        self.numero_atomico = numero_atomico
        self.nome = nome
        self.massa = massa
    
    def printname(self):
        print("Elemento: ", self.elemento, "\nNúmero Atômico: ", self.numero_atomico, "\nNome: ", self.nome, "\nMassa: ", self.massa)

elemento_dict = {
    "Br":  elementos("Br", "35", "Bromo", "79,904"),
    "Cu": elementos("Cu", "29", "Cobre", "63,546"),
    "Be": elementos("Be", "4", "Berilio", "9,0122"),
    "Ti": elementos("Ti", "22", "Titânio", "47,867"),
    "Hg": elementos("Hg", "80", "Mercúrio", "200,59")
}


usuario_elemento = input("Digite o elemento: ")

if usuario_elemento in elemento_dict:
    elemento_dict[usuario_elemento].printname()
else:
    usuario_resposta = input("Elemento não disponível neste programa. Gostaria de ver quais elementos estão disponíveis para ver?\n(sim/não)")

    if usuario_resposta != "sim":
        print("Programa encerrado.")
    else:
        for todos_elementos in elemento_dict:
            print(todos_elementos)