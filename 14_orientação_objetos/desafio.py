class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self): # argumento self é padrão da linguagem, explícita.
        print('Plim Plim')

    def parar(self):
        print('Parando...')
        print('Bicicleta parada.')

    def correr(self):
        print('Vrummmm')

    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}'

bicicleta_1 = Bicicleta('vermelha', 'caloi', 2022, 600)
bicicleta_1.buzinar()
bicicleta_1.correr()
bicicleta_1.parar()

print(bicicleta_1)

