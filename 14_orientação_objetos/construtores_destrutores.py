""" Construtores e Destrutores """

class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print('Removendo a instancia da classe.')

    def latir(self):
        print('auauauau')

cachorro_1 = Cachorro('Bartô', 'tricolor')
cachorro_1.latir()

# também pode ser chamado através da palavra reservada del

del cachorro_1