class candidatos:
    def __init__(self, nome, vice, partido, numero):
        self.nome = nome
        self.vice = vice
        self.partido = partido
        self.numero = numero
        
    def printname(self):
        return f"{self.nome}, {self.vice}, {self.partido}, {self.numero}"

user_candidato = input("Digite o número do partido:\n")

candidatos_dict = {
    "13": candidatos("João", "Maria", "AESSEBR", "13"),
    "22": candidatos("Pedro", "Ana", "RB", "22"),
    "666": candidatos("Davy Jones", "Krauser", "BSDM", "666"),
    "777": candidatos("Bolsonaro", "Jailson Mendes", "SBCMO", "777"),
    "999": candidatos("Kenye West", "Saul Goodman", "KKK", "999")
}

print(candidatos_dict[user_candidato].printname())