from ProdutoVenda import ProdutoVenda


class Venda:
    def __init__(self):
        self._produtos = []
        self._total = 0.0

    @property
    def total(self):
        return self._total

    @property
    def numero_produtos(self):
        return len(self._produtos)

    def adiciona_produto(self, produto: ProdutoVenda):
        self._produtos.append(produto)
        self._total += produto.total

    def __str__(self):
        texto = "\n" + "-" * 50
        texto += "\nProdutos:"

        for produto in self._produtos:
            texto += "\n" + str(produto)

        texto += "\n" + "-" * 50
        texto += "Total da venda: ${t:0.2f}".format(t=self._total)
        texto += "\n" + "-" * 50

        return texto

    def pergunta(mensagem, tipo=int):
        while True:
            try:
                resp = input(mensagem)
                return tipo(resp)
            except:
                print("Valor inválido! Informe novamente.")

    def confirma(mensagem, resposta):
        texto = input(mensagem).strip()
        if texto.lower() == resposta.lower():
            return True
        return False
