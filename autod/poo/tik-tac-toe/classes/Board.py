class Tabuleiro:

    def __init__(self):
        self._posicoes = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def imprime(self):
        print("\n |A|B|C")
        for cont, linha in enumerate(self._posicoes):
            print("--------")
            print(cont + 1, "|" + "|".join(linha), sep="")

    def jogada(self, posicao, simbolo):
        try:
            linha = int(posicao[0]) - 1
            letra = posicao[1].upper()
            coluna = ord(letra) - ord("A")

            if self._posicoes[linha][coluna] == " ":
                self._posicoes[linha][coluna] = simbolo
                return True
        except:
            pass
        return False
    
    def tem_jogada(self):
        for linha in self._posicoes:
            if ' ' in linha:
                return True
        return False
    
    def todas_linhas(self):
        todas = []
        for linha in self._posicoes:
            todas.append(tuple(linha))
        
        for cont in range(3):
            coluna = [
                self._posicoes[0][cont],
                self._posicoes[1][cont],
                self._posicoes[2][cont]
            ]
            todas.append(tuple(coluna))
        
        diagonal = []
        transversal = []
        for cont in range(3):
            diagonal.append(self._posicoes[cont][cont])
            transversal.append(self._posicoes[2 - cont][cont])
        todas.append(tuple(diagonal))
        todas.append(tuple(transversal))
        return todas            
