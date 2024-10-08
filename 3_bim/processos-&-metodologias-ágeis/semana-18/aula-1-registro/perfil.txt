class Perfil(object):
    def __init__(self,nome,telefone,empresa):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
        self.__curtidas = 0

    def imprimir(self):
        print("Nome:%s, Telefone:%s, Empresa:%s" % (self.nome,self.telefone,self.empresa))

    def curtir(self):
        self.__curtidas += 1

    def obter_curtidas(self):
        return self.__curtidas

perfil = Perfil('Luis', 'Não informado', 'Gerson Produções')
perfil.imprimir()

perfil.curtir()
perfil.curtir()

print("Curtidas: %d" % perfil.obter_curtidas())