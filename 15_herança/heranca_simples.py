class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
    
    def ligar_motor(self):
        print('Ligando motor.')

    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}'


class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas) # invocado da classe pai
        self.carregado = carregado
        
    def estar_carregado(self): # método exclusivo da classe. definido para esse escopo em particular
        print(f'{'Sim' if self.carregado else 'Não'} estou carregado.')


moto = Motocicleta('preto', 'abc-1234', 2, )
moto.ligar_motor()

carro = Carro('branco', 'xbe-0098', 4)
carro.ligar_motor()

caminhao = Caminhao('azul', 'gft-8712', 8, True)
caminhao.ligar_motor()
caminhao.estar_carregado()

print(moto)
print(carro)
print(caminhao)