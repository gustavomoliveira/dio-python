""" Listas """

frutas = ['laranja', 'maca', 'uva']

frutas = []

# criação de lista através de construtor. pede um argumento interável, por isso o uso de uma string
letras = list('python')
print(letras)

# função range, mesma do for, printa valores de 0 a 9
os_numeros = list(range(10))
print(os_numeros)

carro = ['Ferrari', 'F8', 4200000, 2020, 2900, 'São Paulo', True]
print(carro)

# matriz bidimensional
matriz = [
    [1, 'a', 2],
    ['b', 3, 4],
    [6, 5, 'c']
]

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

# fatiando

lista = ['p', 'y', 't', 'h', 'o', 'n']

print(lista[2:])
print(lista[0:2])
print(lista[1:3])
print(lista[0:3:2])
print(lista[::]) # mesma lista
print(lista[::-1]) # de trás para frente

veiculos = ['gol', 'celta', 'palio']

# recurso enumerate
for indice, veiculo in enumerate(veiculos):
    print(f'{indice}: {veiculo}')

# recurso list comprehension (pode ser usado com dictionary e tuple)
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
quadrado = [numero ** 2 for numero in numeros]

print(pares)
print(quadrado)

# método copy(): cria uma cópia da lista
# método extend(): junta uma lista com uma nova que é passada com argumento no método
# método index(): qual a primeira ocorrência do parâmetro passado no método
# método pop(): retira sempre o último da lista, mas é possível passar o index como parâmetro. 
# PYTHON TRABALHA COM ESTRUTURA DE PILHAS!
# método remove(): outro método de retirada de elementos da lista. ao invés de passar o index, se passa o objeto em si.
# método reverse(): método de espelhamento de lista.