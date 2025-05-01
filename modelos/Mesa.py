from abstratos.AbstractMesa import *
from modelos.Carta import *


class Mesa(AbstractMesa):

    #Construtor fornecido, nao deve ser alterado
    def __init__(self, jogador1: Jogador, jogador2: Jogador,
                 carta_jogador1: Carta, carta_jogador2: Carta):
        self.__jogador1 = jogador1
        self.__jogador2 = jogador2
        self.__carta_jogador1 = carta_jogador1
        self.__carta_jogador2 = carta_jogador2

    @property
    def jogador1(self) -> Jogador:
        return self.__jogador1

    @jogador1.setter
    def jogador1(self, jogador1: Jogador):
        if isinstance(jogador1, Jogador):
            self.__jogador1 = jogador1

    @property
    def jogador2(self) -> Jogador:
        return self.__jogador2

    @jogador2.setter
    def jogador2(self, jogador2: Jogador):
        if isinstance(jogador2, Jogador):
            self.__jogador2 = jogador2

    @property
    def carta_jogador1(self) -> Carta:
        return self.__carta_jogador1

    @carta_jogador1.setter
    def carta_jogador1(self, carta_jogador1: Carta):
        if isinstance(carta_jogador1, Carta):
            self.__carta_jogador1 = carta_jogador1

    @property
    def carta_jogador2(self) -> Carta:
        return self.__carta_jogador2

    @carta_jogador2.setter
    def carta_jogador2(self, carta_jogador2: Carta):
        if isinstance(carta_jogador2, Carta):
            self.__carta_jogador2 = carta_jogador2
