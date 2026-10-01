from Produto import Produto


class ProdutoEstoque(Produto):
    def __init__(self, descricao, preco):
        super().__init__(descricao, preco)
        self._estoque = 0.0
        
    def __str__(self):
        texto = super().__str__()
        texto += ', Estoque: {e:0.3f}'.format(e=self._estoque)
        return texto

    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, preco):
        self._preco = preco
    
    @property
    def descricao(self):
        return self._descricao
    
    @descricao.setter
    def descricao(self, descricao):
        self._descricao = descricao
    
    def entrada(self, quantidade):
        self._estoque += quantidade
    
    def saida(self, quantidade):
        if quantidade <= self._estoque:
            self._estoque -= quantidade
            return True
        return False
    

