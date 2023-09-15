class Carro:
    def __init__(self, nome) -> None:
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando')

carro = Carro('Fusca')
carro.acelerar()