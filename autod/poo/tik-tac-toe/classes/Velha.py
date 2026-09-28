from random import random
from Board import Tabuleiro


class Velha:
    def __init__(self):
        self._tabuleiro = Tabuleiro()
        if random() >= 0.5:
            self._jogador = "X"
        else:
            self._jogador = "O"

    def imprime(self):
        print("\n" * 50)
        print("Jogo da velha\n")
        self._tabuleiro.imprime()

    def trocar_jogador(self):
        if self._jogador == 'X':
            self._jogador = 'O'
        else:
            self._jogador = 'X'

    def pega_jogada(self):
        while True:
            self.imprime()
            print('\nJogador', self._jogador)
            posicao = input('Informe a jogada: ')
            if self._tabuleiro.jogada(posicao, self._jogador):
                break

    def eh_vencedor(self, jogador):
        linhas = self._tabuleiro.todas_linhas()
        if(tuple([jogador] * 3) in linhas):
            return True
        return False

    def jogar(self):
        while self._tabuleiro.tem_jogada():
            self.imprime()
            self.pega_jogada()
            
            if(self.eh_vencedor(self._jogador)):
                self.imprime()
                print('\nFim de Jogo!')
                print('Vitória do jogador', self._jogador)
                return
            self.trocar_jogador()
        self.imprime()
        print('\nJogo empatado!')
        
if __name__ == '__main__':
    jogo = Velha()
    jogo.jogar()