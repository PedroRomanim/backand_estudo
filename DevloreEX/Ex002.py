class Carro:
    def __init__(self, cor, modelo, ano):
        self.cor = cor
        self.modelo = modelo 
        self.ano = ano



class Garragem(Carro):
    def __init__(self, cor, modelo, ano):
        super().__init__(cor, modelo, ano)
        self.dono = []

    def proprietario(self, proprietario):
        self.proprietario.append(self.dono)
 
    def info(self):
        print(f"Proprietario: ")
        for proprietario in self.dono:
            print(f"- {self.dono}")
        print(f"Ano do veiculo: {self.ano}")
        print(f"Modelo do veiculo: {self.modelo}")
        print(f"Cor do veiculo: {self.cor}")




