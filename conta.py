
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print(f'A conta do titular {self.titular}, possui um saldo de {self.saldo} reais')

    def deposito(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor
