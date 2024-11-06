""" Funções """

# se não houver return declarado, por padrão, retorna None

# forma de argumentos nomeados
def salvar_carro(marca, modelo, ano, placa):
    print(f'Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}')

salvar_carro('Fiat', 'Palio', 1999, 'ABC-1234') # argumento direto
salvar_carro(marca='Fiat', modelo='Palio', ano=1999, placa='ABC-1234') # argumento nomeado
salvar_carro(**{'marca': 'Fiat', 'modelo': 'Palio', 'ano': 1999, 'placa': 'ABC-1234'}) # definindo argumentos em modelo dicionário

# as funções em Python aceitam argumentos pre definidos usando o símbolo de / e *
# todos os argumentos usados antes da / devem ser de posição
# todos os argumentos usados após o * devem ser por keyword

# objetos de primira classe
def somar(a, b):
    return a + b

# uma função chamando outra função, assim como em JS
def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f'O resultado da operação é {resultado}')

exibir_resultado(10, 10, somar) # ---> a função não precisa de () quando passada como argumento de outra função

# também é possível de realizar um apontamento de uma função para uma variável
teste = somar
print(teste(2, 23))

# Python faz uso de escopo local e global, assim como JS