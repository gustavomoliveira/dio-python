class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade) # cls é a própria classe Pessoa
    
    @staticmethod
    def maior_idade(idade):
        return idade >= 18
    

p = Pessoa.criar_data_nascimento(1987, 4, 20, 'Gustavo')
print(p.nome, p.idade)

print(Pessoa.maior_idade(18))
print(Pessoa.maior_idade(8))