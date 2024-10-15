""" Estruturas de Repetição """

# for - quando sabemos o número total de iterações
""" texto = input('Digite um texto qualquer: ')
VOGAIS = 'AEIOU'

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra)

print() """ # quebra de linha

# for / else
# é possível atribuir ao final, apesar de não muito comum

# função built-in range(start, stop, step)
for numero in range(0, 51, 5):
    print(numero)

# while - quando não sabemos o número total de iterações
""" opcao = -1

while opcao != 0:
    opcao = int(input('[1] Sacar \n[2] Extrato \n[0] Sair \n: '))
    if opcao == 1:
        print('Sacando...')
    elif opcao == 2:
        print('Exibindo extrato...') """

# usando break e continue
contador = 0

while True:
    numero = int(input('Digite um número qualquer: '))
    contador += 1
    if numero == 10:
        break
    print(f'Número digitado: {numero}. Tentativa: {contador}')

# o continue pula a execução se a condição for atendida