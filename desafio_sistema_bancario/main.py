
from datetime import datetime

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

def data_hoje():
    return datetime.now().strftime('%d/%m/%Y')

def resetar_operacoes(dados, operacoes):
    hoje = datetime.now().date()
    if operacoes:
        ultima_operacao = datetime.strptime(operacoes[-1][2], '%d/%m/%Y').date()
        if ultima_operacao < hoje:
            dados[0] = 10

def menu():
    print(
        '-------- MENU ---------\n\n'
        '[1] - Sacar\n'
        '[2] - Depositar\n'
        '[3] - Visualizar\n'
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

def escolher_operacao(dados, operacoes):
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
            case 0:
                print('\nObrigado por usar o nosso sistema!')
                break
            case _:
                print('\nDigite uma opção válida.')

# saques diários, extrato, saldo, limite do saque
dados = [10, '', 5000, 500]
operacoes = []
escolher_operacao(dados, operacoes)
