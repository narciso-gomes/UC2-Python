from Produto import Produto

class ProdutoVenda(Produto):
    
    def __init__(self, descricao, preco, quantidade):
        super().__init__(descricao, preco)
        self._quantidade = quantidade
    
    @property
    def total(self):
        return self._quantidade * self._preco
    
    def __str__(self):
        texto = super().__str__()
        texto += ', Qtde: {q:0.3f}'.format(q=self._quantidade)
        texto += ', Total: ${t:0.2f}'.format(t=self.total)
        return texto
    
        
    