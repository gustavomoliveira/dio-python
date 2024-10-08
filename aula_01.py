print('Hello World!')
print(1 + 10)
print(1.5 + 10)
print(True)
print(False)
print('testando uma string em Python')

""" não existe palavra reservada para determinar variáveis ou constantes em Python """
age = 37
name = 'Gustavo'
""" template literals se usa f antes da frase com {} para as variáveis """
print(f'Meu nome é {name} e eu tenho {age} anos de idade.')

""" variável age e name sendo reatribuídas """
age = 33
name = 'Mari'
print(f'Meu nome é {name} e eu tenho {age} anos de idade.')

""" constante em Python é escrito com maiúsculas; AGE e NAME no caso acima """
""" padrão de nomes em Python é o snake case, ou seja, underline. ex my_age """

""" constante recebendo o valor como array """
ESTADOS = ['SP', 'MG', 'RJ', 'RS']
print(ESTADOS)

""" convertendo tipos """
preco = 10.50
print(preco)

""" int """
preco = int(preco)
print(preco)

preco = 10
print(preco)

""" divisão com uma barra é o mesmo que converter para float """
print(preco / 2)

""" divisão com duas barras o valor int é preservado """
print(preco // 2)

""" string para number(float e int) """
preco = '10.50'
idade = '37'

print(float(preco))
print(int(idade))

""" usar type para verificar qual a classe desse tipo """
print(type(str(100)))
