class Cliente:
    def __init__(self, nome, endereco):
        self._nome = nome
        self._endereco = endereco

    def imprime(self):
        print(f"Cliente: {self._nome}")
        print(f"Endereço: {self._endereco}")


# Herança
class ClientePF(Cliente):
    def __init__(self, nome, endereco, cpf, nascimento):
        super().__init__(nome, endereco)
        self._cpf = cpf
        self._nascimento = nascimento


# Herança
class ClientePJ(Cliente):
    def __init__(self, nome, endereco, cnpj):
        super().__init__(nome, endereco)
        self._cnpj = cnpj
