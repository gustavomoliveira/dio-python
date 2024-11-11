""" Date, Datetime, Time """

# poderia usar o import datetime, mas existe uma forma específica para acessar uma determinada classe
from datetime import date, datetime, time, timezone

data = date(2024, 10, 28)
print(data)

print(date.today()) # data atual

data_hora = datetime(2024, 10, 28, 10, 30, 20) # é passado, também, o horário
print(data_hora)

print(datetime.today())

hora = time(10, 20, 0) # hora
print(hora)

# timedelta
from datetime import timedelta

tipo_carro = 'P' # P, M, G
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == 'P':
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(data_estimada.time())
elif tipo_carro == 'M':
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(data_estimada)
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(data_estimada)


# strftime e strptime para formatar datas e horas
d = datetime.now()

print(d.strftime('%d/%m/%Y %H:%M'))

date_string = '20/07/2024 15:30'
d = datetime.strptime(date_string, '%d/%m/%Y %H:%M')
print(d)

# timezones
# biblioteca pytz

# criando timezones somento com python, sem biblioteca
data_oslo = datetime.now(timezone(timedelta(hours=2)))
data_sao_paulo = datetime.now(timezone(timedelta(hours=-3)))
print(data_oslo)
print(data_sao_paulo)
