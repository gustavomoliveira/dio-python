""" Manipulação de Strings """

# upper(), lower(), title()
# strip(), lstrip(), rstrip() - remove espaços em branco

# center() e join()
curso = 'Python'
print(curso.center(10, '#')) # ---> número de caracteres e o caracter em si. centraliza a string

print('.'.join(curso)) # ---> como em JS. insere o caracter passado entre os caracteres da string


""" Interpolação de variáveis """

# %(old), format(old) e f-string

nome = 'Gustavo'
idade = 37
dados = {'nome': 'Gustavo', 'idade': 37}

# %
print('Nome: %s Idade: %d' % (nome, idade))

# format
print('Nome: {} Idade: {}'.format(nome, idade))
print('Nome: {nome} Idade: {idade}'.format(**dados)) # ---> utilizando dicionário
print('Nome: {nome} Idade: {idade}'.format(nome=nome, idade=idade)) # ---> nomeando as chaves
print('Nome: {1} Idade: {0}'.format(idade, nome)) # ---> passando os índices

# f-string
print(f'A idade é {idade:.2f}')
print(f'A idade é {idade:10.2f}') # ---> o primeiro argumento é o número de espaços

""" Fatiamento de Strings """

# start, stop e step
o_nome = 'Gustavo Mendes de Oliveira'

print(o_nome[0]) # o caracter exato
print(o_nome[:9]) # sem início e com final
print(o_nome[10:]) # com início e sem final
print(o_nome[10:16]) # com início e com final
print(o_nome[10:16:2]) # com início, final e número definido do passo
print(o_nome[:]) # retorna a mesma string
print(o_nome[::-1]) # faz o espelhamento da string

""" String Multilinhas """

pet = 'cachorro'
mensagem = f""" 
Olá, eu tenho um {pet}
    que se chama Bartolomeu.
""" # respeita recuos. perfeito para menus.

print(mensagem)
