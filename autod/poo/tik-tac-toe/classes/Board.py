class Tabuleiro:

    def __init__(self):
        self._posicoes = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def imprime(self):
        print("\n |A|B|C")
        for cont, linha in enumerate(self._posicoes):
            print("--------")
            print(cont + 1, "|" + "|".join(linha), sep="")


tabuleiro = Tabuleiro()

tabuleiro.imprime()
