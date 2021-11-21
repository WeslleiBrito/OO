
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'A conta do titular {self.__titular}, possui um saldo de {self.__saldo} reais')

    def deposito(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor
