class Pessoa:
    def __init__(self, nome) -> None:
        self.nome = nome
        # self referencia a classe

# p1 = Pessoa()
# p1.nome = 'Bianca'
# print(p1)
# print(p1.nome)

p1 = Pessoa('Bianca')
print(p1.nome)