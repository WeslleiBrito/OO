
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'A conta do titular {self.__titular}, possui um saldo de {self.__saldo} reais')

    def depositar(self, valor):
        self.__saldo += valor

    def __autoriza_retirada(self, valor):
        saldo_limite = self.__saldo + self.limite
        return valor <= saldo_limite

    def sacar(self, valor):
        if self.__autoriza_retirada(valor):
            self.__saldo -= valor
        else:
            print(f'Valor de {valor} excede o saldo e o limite de sua conta que é de {self.__saldo + self.limite}')

    def transferir(self, valor, conta_destino):
        if self.__autoriza_retirada(valor):
            self.sacar(valor)
            conta_destino.depositar(valor)
        else:
            print(f'Valor de {valor} excede o saldo e o limite de sua conta que é de {self.__saldo + self.limite}')

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        self.__limite = valor

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor

    @staticmethod
    def codigo_banco():
        return '001'

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}
