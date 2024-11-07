# 1 - limite de 10 transações, sejam elas saque ou depósitos, por dia (armazenar data para comparação)
# 2 - se o usuário tentar afzer uma transação após atingir o limite, deve ser informado que ele excedeu o número de transações
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

def sacar(saques, limite, saldo, valor, extrato):
    if saldo < valor:
        return saques, saldo, extrato, '\nSaldo indisponível. Não é possível realizar a transação.\n'
    if saques <= 0:
        return saques, saldo, extrato, '\nLimite de saques diário excedido.\n'
    if limite < valor:
        return saques, saldo, extrato, '\nO valor limite permitido por saque é de R$500,00.\n'
    
    saldo -= valor
    saques -= 1
    extrato += f'Saque: R${valor:.2f}.\n'
    return saques, saldo, extrato, f'\nSaque de R${valor:.2f} realizado com sucesso!\n'
  
def depositar(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R${valor:.2f}.\n'
        return saldo, extrato, f'\nDepósito de R${valor:.2f} realizado com sucesso!\n'
    else:
        return '\nValor incorreto. Insira novamente.\n'
    
def exibir_extrato(extrato, saldo):
    if not extrato:
        print('\nNão foram realizadas movimentações.\n')
    else:
        print(f'\n----- EXTRATO -----\n')
        print(f'{extrato}')
        print(f'Saldo total: R${saldo:.2f}')
        print('\n--------------------\n')  
    return extrato

def escolher_operacao(saques, limite, saldo, extrato):
    while True:
        menu()
        opcao = validar_opcao('Digite a operação deseja realizar: ')

        match opcao:
            case 1:
                valor_saque = validar_valor('Digite o valor desejado para saque: ')
                saques, saldo, extrato, mensagem_saque = sacar(saques, limite, saldo, valor_saque, extrato)
                print(mensagem_saque)
            case 2:
                valor_deposito = validar_valor('Digite o valor desejado para depósito: ')
                saldo, extrato, mensagem_deposito = depositar(valor_deposito, saldo, extrato)
                print(mensagem_deposito)
            case 3:
                exibir_extrato(extrato, saldo)
            case 0:
                print('\nObrigado por usar o nosso sistema!')
                break
            case _:
                print('\nDigite uma opção válida.')

numero_saque_diario = 3 # numero de saques diários permitidos
extrato = '' # extrato
saldo = 5000 # saldo inicial é de 0
limite = 500 # limite de valor de cada saque
escolher_operacao(numero_saque_diario, limite, saldo, extrato)

