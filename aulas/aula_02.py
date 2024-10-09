""" função input(). retorna o valor convertido em string. sintax -- input(prompt) """
""" 
nome = input('Digite seu nome: ')
print(f'Meu nome é {nome.capitalize()}') """

""" função print(). sintax -- print(object(s), sep=separator, end=end, file=file, flush=flush) """

name = 'Gustavo'
sur_name = 'de Oliveira'

print(name, sur_name)

""" parâmetro opcional end necessita de quebra de linha """
print(name, sur_name, end='!\n')
print(name, sur_name, sep='~')
