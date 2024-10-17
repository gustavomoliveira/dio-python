numero_saque_diario = 3
extrato = ''
saldo = 0
limite = 500

menu =""" 
--------------- MENU ---------------
            [1] - Sacar
            [2] - Depositar
            [3] - Visualizar
            [0] - Sair
------------------------------------
Digite o número da operação desejada:
"""

def saque(saques, limite, saldo, valor, extrato):
    if saldo > valor:
        if saques > 0:
            if limite >= valor:
                saldo -= valor
                saques -= 1
                extrato += f'Saque: R${valor:.2f}.\n'
                return saques, saldo, extrato, f'Saque de R${valor:.2f} realizado com sucesso!'
            else:
                return saques, saldo, extrato, f'O valor limite permitido por saque é de R$500,00.'
        else:
            return saques, saldo, extrato, f'Limite de saques diário excedido. Tente novamente amanhã.'
    else:
        return saques, saldo, extrato, f'Saldo indisponível. Não é possível realizar a transação.'
    

def deposito(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R${valor:.2f}.\n'
        return saldo, extrato, f'Depósito de R${valor:.2f} realizado com sucesso!'
    else:
        return 'Valor incorreto. Insira novamente.'
    
def exibir_extrato(extrato, saldo):
    if not extrato:
        print('Não foram realizadas movimentações.')
    else:
        print(f""" 
----- EXTRATO -----
{extrato}
Saldo total: R${saldo:.2f}
 """)
    return extrato


while True:
    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input('Digite o valor desejado para saque: '))
        numero_saque_diario, saldo, extrato, mensagem = saque(numero_saque_diario, limite, saldo, valor, extrato)
        print(mensagem)
    elif opcao == 2:
        valor = float(input('Digite o valor desejado para depósito: '))
        saldo, extrato, mensagem = deposito(valor, saldo, extrato)
        print(mensagem)
    elif opcao == 3:
        exibir_extrato(extrato, saldo)
    elif opcao == 0:
        print('Obrigado por usar o nosso sistema.')
        break
    else:
        print('Digite uma opção válida.')
