class Passaro:
    def voar(self):
        print('Voando')

class Pardal(Passaro):
    def voar(self):
        return super().voar() # implementação da classe pai
    
class Avestruz(Passaro):
    def voar(self):
        print('Não pdoe voar')

def plano_voo(obj):
    obj.voar()

p1 = Pardal()
p2 = Avestruz()

plano_voo(p1)
plano_voo(p2)