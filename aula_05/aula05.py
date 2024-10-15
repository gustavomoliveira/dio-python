""" Condicionais """

# 1 - if / elif / else

""" MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input('Informe a sua idade: '))

if idade >= MAIOR_IDADE:
    print('Pode tirar a CNH.')
elif idade == IDADE_ESPECIAL:
    print('Pode iniciar as aulas teóricas.')
else:
    print('Não pode tirar a CNH.') """


# 2 - if aninhado

menu = int(input(""" 
----- MENU -----
[1] - Conta Padrão
[2] - Conta Universitária
----------------
"""))

saldo = 2000
saque = 500
cheque_especial = 450

if menu == 1:
    if saldo >= saque:
        print('Saque realizado com sucesso!')
    elif saque <= (saldo + cheque_especial):
        print('Saque realizado com uso do cheque especial.')
    else:
        print('Saldo insuficiente.')
elif menu == 2:
    if saldo >= saque:
        print('Saque realizado com sucesso!')
    else:
        print('Saldo insuficiente.')
else:
    print('Opção inválida. Selecione uma conta válida.')


""" 3 - if ternário """

# estrutura diferente de JS. a primeira parte retorna se True. ao final retorna se False
status = 'Sucesso' if saldo >= saque else 'Falha'
print(f'{status} ao realizar o saque!')