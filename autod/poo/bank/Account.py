from Client import *


class Conta:

    _quantidade = 0

    @classmethod
    def adiciona(cls):
        cls._quantidade += 1

    @classmethod
    def quantidade(cls):
        return cls._quantidade

    @classmethod
    def imprimir_quantidade(cls):
        print("#" * 30)
        print(f"Total de Contas: {cls.quantidade()}")
        print("#" * 30)

    def __init__(self, numero, cliente: ClientePF | ClientePJ):
        self.adiciona()
        self._numero = numero
        self._saldo = 0.0

        # Agregação -> a classe Conta recebe a Classe Cliente
        self._cliente = cliente

    # Encapsulamento
    def depositar(self, valor):
        self._saldo += valor

    def saldo(self):
        return self._saldo

    def numero(self):
        return self._numero

    def cliente_nome(self):
        return self._cliente._nome

    def sacar(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
            return True
        return False

    def transferir(self, destino: Conta, valor):
        if self.sacar(valor):
            destino.depositar(valor)
            return True
        return False

    def imprimir(self):
        print("#" * 30)
        print(f"Conta: {self.numero()}")
        print(f"Cliente: {self.cliente_nome()} - {type(self._cliente)}")
        print(f"Saldo (R$): {self.saldo()}")
        print("#" * 30)


class ContaInvestimento(Conta):
    
    # Polimorfismo
    def depositar(self, valor):
        self._saldo += valor * 1.01