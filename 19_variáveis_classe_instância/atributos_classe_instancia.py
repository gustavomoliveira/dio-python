class Estudante:
    escola = 'Infnet' # variável de classe

    def __init__(self, nome, matricula):
        self.nome = nome # atributo de instância
        self.matricula = matricula

    def __str__(self):
        return f'{self.nome} - {self.matricula} - {self.escola}'
    

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)
    
aluno1 = Estudante('Gustavo', 123)
aluno2 = Estudante('Mari', 456)
mostrar_valores(aluno1, aluno2)


Estudante.escola = 'Python' # quando a variável de classe é trocada, todos as instâncias dessa classe recebem o novo valor
aluno1.matricula = 387

aluno3 = Estudante('Bartô', 768) # criando um novo aluno após a definição da variável de classe
mostrar_valores(aluno1, aluno2, aluno3)