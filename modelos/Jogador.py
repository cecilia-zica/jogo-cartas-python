from abstratos.AbstractJogador import *
from modelos.Carta import Carta


class Jogador(AbstractJogador):

    def __init__(self, nome: str):
        self.__nome = nome
        self.__mao = []

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    def baixa_carta_da_mao(self) -> Carta:
        if not self.__mao:
            raise ValueError("O jogador não possui cartas na mão.")
        return self.__mao.pop(0)

    @property
    def mao(self) -> list:
        return self.__mao

    @mao.setter
    def mao(self, mao: list):
        if isinstance(mao, list):
            self.__mao = mao

    def inclui_carta_na_mao(self, carta:Carta):
        self.__mao.append(carta)
