from utilitarios import *

def menu():
    print(
        '-------- MENU ---------\n\n'
        '[1] - Sacar\n'
        '[2] - Depositar\n'
        '[3] - Visualizar\n'
        '[4] - Cadastrar Usuário\n'
        '[5] - Cadastrar Conta\n'
        '[6] - Exibir Contas\n'
        '[0] - Sair\n\n'
        '-----------------------\n'
        )

def sacar(dados, valor, operacoes):
    if dados[2] < valor:
        return '\nSaldo indisponível. Não é possível realizar a transação.\n'
    if dados[0] <= 0:
        return '\nLimite de operações diárias excedido.\n'
    if dados[3] < valor:
        return '\nO valor limite permitido por saque é de R$500,00.\n'
        
    dados[2] -= valor
    dados[0] -= 1
    dados[1] += f'Saque: R${valor:.2f}.\n'

    oper_saque = ['Saque', valor, data_hoje()]
    operacoes.append(oper_saque)

    return f'\nSaque de R${valor:.2f} realizado com sucesso!\n'
  
def depositar(valor, dados, operacoes):
    if dados[0] <= 0:
        return '\nLimite de operações diárias excedido.\n'

    if valor > 0:
        dados[2] += valor
        dados[0] -= 1
        dados[1] += f'Depósito: R${valor:.2f}.\n'

        oper_deposito = ['Depósito', valor, data_hoje()]
        operacoes.append(oper_deposito)

        return f'\nDepósito de R${valor:.2f} realizado com sucesso!\n'
    else:
        return '\nValor incorreto. Insira novamente.\n'
 
def exibir_extrato(dados, operacoes):
    if not operacoes:
        print('\nNão foram realizadas movimentações.\n')
    else:
        print(f'\n----- EXTRATO -----\n')
        for operacao in operacoes:
            print(f'{operacao[0]}: R${operacao[1]:.2f}')
            print(f'Data: {operacao[2]}\n')
        print(f'Operações Restantes no Dia: {dados[0]}')
        print(f'Saldo total: R${dados[2]:.2f}')
        print('\n--------------------\n')
     
def cadastrar_usuario(usuarios):
    endereco = ''
    while True:
        nome = validar_texto('Digite o nome para cadastro: ')
        nascimento = validar_nascimento('Digite sua data de nascimento (Formato: dd/mm/aaaa): ')
        cpf = validar_duplicidade_cpf(usuarios, 'Digite o seu CPF (apenas números): ')
        
        logradouro = validar_texto('Digite o nome de sua rua de residência (apenas a rua/avenida, sem números ou bairro): ')
        endereco += logradouro + ''
        
        num = validar_num_endereco('Digite o número da sua residência: ')
        endereco += ' ' + num + ' '
        
        cidade = validar_cidade('Digite a sua cidade e estado(Formato: cidade/sigla): ')
        endereco += cidade + '.'
        
        cadastro = [nome, nascimento, cpf, endereco, []]
        usuarios.append(cadastro)
        print('\nCadastro realizado com sucesso!\n')
        print('Dados do cadastro:\n')
        print(f'Nome: {nome}')
        print(f'Data de nascimento: {nascimento}')
        print(f'CPF: {cpf}')
        print(f'Endereço: {endereco}')
        print('\n----------------------------------\n')
        endereco = ''

        seguir = validar_seguir('Deseja realizar outro cadastro?(Digite "s/n"): ')
        if seguir == 'n':
            print('\nCadastro de usuário finalizado.\n')
            break
    

def cadastrar_conta(usuarios, contador):
    conta_usuario = validar_entrada_cpf('Digite o CPF do usuário (apenas números): ')

    for usuario in usuarios:
        if usuario[2] == conta_usuario:
            agencia = '0001'
            num_conta = contador
            conta = [num_conta, agencia]
            usuario[4].append(conta)
            print(f'\nConta cadastrada com sucesso para o usuário {usuario[0]}!\n')
            print(f'Conta: {conta[0]}, Agência: {conta[1]}\n')
            return contador + 1
        
    novo_cadastro = validar_seguir('\nUsuário não encontrado. Deseja cadastrar um novo usuário?(Digite "s/n"):\n')
    if novo_cadastro == 's':
        cadastrar_usuario(usuarios)
    else:
        print('\nCadastro de Conta encerrado.')
    return contador

def exibir_contas(usuarios):
    print(f'\n----- Contas Cadastradas -----\n')
    for usuario in usuarios:
        if not usuario[4]:
            print('Não foram encontradas contas cadastradas.\n')
        else:
            print(f'Usuário: {usuario[0]}\n')
            print(f'CPF: {usuario[2]}\n')
            for conta in usuario[4]:
                print(f'Conta Corrente: {conta[0]}\n')
                print(f'Agência: {conta[1]}\n')
    print('----------------------------------\n')

def escolher_operacao(dados, operacoes, usuarios, contador):
    while True:
        resetar_operacoes(dados, operacoes)
        menu()
        opcao = validar_opcao('Digite a operação deseja realizar: ')

        match opcao:
            case 1:
                valor_saque = validar_valor('Digite o valor desejado para saque: ')
                mensagem_saque = sacar(dados, valor_saque, operacoes)
                print(mensagem_saque)
            case 2:
                valor_deposito = validar_valor('Digite o valor desejado para depósito: ')
                mensagem_deposito = depositar(valor_deposito, dados, operacoes)
                print(mensagem_deposito)
            case 3:
                exibir_extrato(dados, operacoes)
            case 4:
                cadastrar_usuario(usuarios)
            case 5:
                contador = cadastrar_conta(usuarios, contador)
            case 6:
                exibir_contas(usuarios)
            case 0:
                print('\nObrigado por usar o nosso sistema!\n')
                break
            case _:
                print('\nDigite uma opção válida.')

# saques diários, extrato, saldo, limite do saque
dados = [10, '', 5000, 500]
operacoes = []
usuarios = []
contador_geral_contas = 1
escolher_operacao(dados, operacoes, usuarios, contador_geral_contas)



