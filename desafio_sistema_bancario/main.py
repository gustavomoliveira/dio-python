# 1 - limite de 10 transações, sejam elas saque ou depósitos, por dia (armazenar data para comparação)
# 2 - se o usuário tentar fazer uma transação após atingir o limite, deve ser informado que ele excedeu o número de transações
# permitidas para aquele dia
# 3 - Mostre no extrato a data e hora de todas as transações (operações)

def validar_opcao(msg):
    while True:
        try:
            opcao = int(input(msg))
            if 0 <= opcao <= 3:
                return opcao
            else:
                print('ERRO: Selecione uma opção válida no Menu.')
        except ValueError:
            print('ERRO: Digite apenas números inteiros.')

def validar_valor(msg):
    while True:
        try:
            valor = float(input(msg))
            return valor
        except ValueError:
            print('ERRO: Digite um número válido.')

def menu():
    print(
        '-------- MENU ---------\n\n'
        '[1] - Sacar\n'
        '[2] - Depositar\n'
        '[3] - Visualizar\n'
        '[0] - Sair\n\n'
        '-----------------------\n'
        )

def sacar(dados, valor):
    if dados[2] < valor:
        return '\nSaldo indisponível. Não é possível realizar a transação.\n'
    if dados[0] <= 0:
        return '\nLimite de saques diário excedido.\n'
    if dados[3] < valor:
        return '\nO valor limite permitido por saque é de R$500,00.\n'
        
    dados[2] -= valor
    dados[0] -= 1
    dados[1] += f'Saque: R${valor:.2f}.\n'
    return f'\nSaque de R${valor:.2f} realizado com sucesso!\n'
  
def depositar(valor, dados):
    if valor > 0:
        dados[2] += valor
        dados[1] += f'Depósito: R${valor:.2f}.\n'
        return f'\nDepósito de R${valor:.2f} realizado com sucesso!\n'
    else:
        return '\nValor incorreto. Insira novamente.\n'
    
def exibir_extrato(dados):
    if not dados[1]:
        print('\nNão foram realizadas movimentações.\n')
    else:
        print(f'\n----- EXTRATO -----\n')
        print(f'{dados[1]}')
        print(f'Saldo total: R${dados[2]:.2f}')
        print('\n--------------------\n')

def escolher_operacao(dados):
    while True:
        menu()
        opcao = validar_opcao('Digite a operação deseja realizar: ')

        match opcao:
            case 1:
                valor_saque = validar_valor('Digite o valor desejado para saque: ')
                mensagem_saque = sacar(dados, valor_saque)
                print(mensagem_saque)
            case 2:
                valor_deposito = validar_valor('Digite o valor desejado para depósito: ')
                mensagem_deposito = depositar(valor_deposito, dados)
                print(mensagem_deposito)
            case 3:
                exibir_extrato(dados)
            case 0:
                print('\nObrigado por usar o nosso sistema!')
                break
            case _:
                print('\nDigite uma opção válida.')

# n˚ de saques diários, extrato, saldo, limite do saque
dados = [3, '', 5000, 500]
escolher_operacao(dados)

