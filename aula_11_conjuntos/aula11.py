""" Conjuntos """

# Estrutura de dados set elimina duplicatas. o construtor espera um iterável.

# IMPORTANTE: set() não garante a ordem!
print(set([1, 2, 3, 1, 3, 4]))
print(set('abacaxi'))
print(set(('palio', 'gol', 'celta', 'palio')))

# escrita sempre com {}

# conjuntos não suportam indexação: [0], [-1], etc. É necessário, primeiro, realizar uma conversão para lista
numeros = {1, 2, 3, 2}
numeros = list(numeros)
numeros = [0]

# porém, é possível iterar com um loop dentro de um set
carros = {'GLC', 'X5', 'Q8'}

for carro in carros:
    print(carro)

# também possui enumerate
for indice, carro in enumerate(carros):
    print(f'{indice}: {carro}')

# Métodos de set

# {}.union -> une eliminando repetição, caso exista
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
print(conjunto_a.union(conjunto_b))

# {}.intersection -> pega apenas apenas os valores repetidos
print(conjunto_a.intersection(conjunto_b))

# {}.difference -> tudo o que contém em um, mas não no outro
print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))

# {}.symmetric_difference -> tudo o que não se repete, a diferença de ambos
print(conjunto_a.symmetric_difference(conjunto_b))

# {}.issubset -> se todos os elementos de um set pertencem a outro
conjunto_c = {1, 2, 3}
conjunto_d = {4, 1, 2, 5, 6, 3}

print(conjunto_c.issubset(conjunto_d)) # True
print(conjunto_d.issubset(conjunto_c)) # False

# {}.issuperset - > o oposto de .issubset
print(conjunto_c.issuperset(conjunto_d)) # False
print(conjunto_d.issuperset(conjunto_c)) # True

# {}.isdisjoint -> verifica se tudo o que está em um não está em outro, retorna True caso verdadeiro
conjunto_f = {0}

print(conjunto_c.isdisjoint(conjunto_f)) # True
print(conjunto_c.isdisjoint(conjunto_d)) # False

# {}.add -> se não existir, o elemento passado como parâmetro é adicionado ao final do set
sorteio = {1, 23}

sorteio.add(25)
print(sorteio)
sorteio.add(42)
print(sorteio)
sorteio.add(25) # já existe
print(sorteio)
