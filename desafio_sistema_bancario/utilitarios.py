""" Funções utilitárias """

from datetime import datetime
import re

def validar_opcao(msg):
    while True:
        try:
            opcao = int(input(msg))
            if 0 <= opcao <= 6:
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

def validar_texto(msg):
    while True:
        try:
            texto = input(msg).title()
            if all(letra.isalpha() or letra.isspace() for letra in texto):
                return texto
            else:
                print('ERRO: Texto inválido.')
        except ValueError:
            print('ERRO: Digite apenas caracteres válidos.')

def validar_seguir(msg):
    while True:
        try:
            seguir = input(msg).lower()
            if seguir == 's' or seguir == 'n':
                return seguir
            else:
                print('ERRO: Digite "s/n".')
        except ValueError:
            print('ERRO: Digite uma opção válida.')

def validar_num_endereco(msg):
    while True:
        try:
            num = str(input(msg))
            if all(char.isnumeric() for char in num):
                return num
            else:
                print('ERRO: Digite apenas caracteres válidos.')
        except ValueError:
            print('ERRO: Digite um número válido.')

def validar_nascimento(msg):
    while True:
        try:
            nascimento = input(msg)
            padrao_nascimento = r'^\d{2}/\d{2}/\d{4}$'
            if re.match(padrao_nascimento, nascimento):
                return nascimento
            else:
                print('ERRO: Entrada inválida. A data de nascimento deve ser no padrão dd/mm/aaaa.')
        except ValueError:
            print('ERRO: Digite apenas caracteres válidos.')

def validar_entrada_cpf(msg):
    while True:
        cpf = str(input(msg))
        if cpf.isnumeric() and len(cpf) == 11:
            return cpf
        else:
            print('ERRO: O CPF deve conter 11 números e apenas números.')

def validar_duplicidade_cpf(usuarios, msg):
    while True:
        cpf = validar_entrada_cpf(msg)
        duplicado = False
        
        for dados in usuarios:
            if cpf == dados[2]:
                print('ERRO: CPF já cadastrado. Tente novamente.')
                duplicado = True
                break
        
        if not duplicado:
            return cpf

def validar_cidade(msg):
    while True:
        try:
            entrada = input(msg).upper()
            padrao = r"^[a-zA-Z]+(?: [a-zA-Z]+)*/[a-zA-Z]{2}$"
            if re.match(padrao, entrada):
                return entrada
            else:
                print('ERRO: Entrada inválida. Por favor, use o formato "cidade/sigla".')
        except ValueError:
            print('ERRO: Digite apenas caracteres válidos.')    

def data_hoje():
    return datetime.now().strftime('%d/%m/%Y')

def resetar_operacoes(dados, operacoes):
    hoje = datetime.now().date()
    if operacoes:
        ultima_operacao = datetime.strptime(operacoes[-1][2], '%d/%m/%Y').date()
        if ultima_operacao < hoje:
            dados[0] = 10