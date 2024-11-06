""" Dicionários """

# Para se criar um dicionário, os valores precisam ser imutáveis.
# A lista, que é mutável, não pode ser adicionada a um diconário como chave, key. Apenas os valores pode ser mutáveis.

# Exemplo de dicionário aninhado
contatos = {
    'gustavo@gmail.com': {'nome': 'Gustavo', 'telefone': '99999-9999'},
    'barto@gmail.com': {'nome': 'Bartô', 'telefone': '99999-9998'},
    'mari@gmail.com': {'nome': 'Mari', 'telefone': '99999-9979'},
}

print(contatos['gustavo@gmail.com']['telefone'])

# Forma eficiente de percorrer um dicionário utilizando o método items()
for chave, valor in contatos.items():
    print(chave, valor)

