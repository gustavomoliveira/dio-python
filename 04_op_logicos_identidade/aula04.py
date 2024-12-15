""" Operadores Lógicos """

# and - para ser True tudo precisa ser True
# or - para ser True apenas um precisa ser True
# not - negação da afirmação

saldo = 1000
saque = 250
limite = 200
conta_especial = True

# comparação extensa, sem uso de variável, legibilidade ruim
print (saldo >= saque and saque <= limite or conta_especial and saldo >= saque)
print ((saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque))

# melhores práticas, legibilidade boa
conta_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque
exp = conta_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp)

""" Operadores de Identidade """

# is - objeto vs objeto, se ocupa a mesma região de memória
# is not - compara para verificar o contrário

valor = 1000
total = 500

print(valor is total)
print(valor is not total)

""" Operadores de Associação """

# in - se pertence (case sensitive)
# not in - se não pertence

curso = 'Curso de Python'
frutas = ['laranja', 'uva', 'limão']
saques = [1500, 100]

print('Python' in curso)
print('maçã' not in frutas)
print(200 in saques)