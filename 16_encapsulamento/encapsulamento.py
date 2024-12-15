# todo acesso em python é público, já que a linguagem é fracamente tipada
# não existe garantia de bloqueio a acessos privados em python
# a convenção é o uso de _ para demonstrar que aquela variável ou método são privados

class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo # privado
        self.nro_agencia = nro_agencia # público

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def mostrar_saldo(self):
        return self._saldo

conta = Conta('001', 100)

print(conta._saldo) # errado
print(conta.nro_agencia) # correto
print(conta.mostrar_saldo()) # a forma correta de acessar o saldo, criando um método específico para isso