from abstratos.AbstractCarta import *
from modelos.Personagem import Personagem



class Carta(AbstractCarta):

    def __init__(self, personagem: Personagem):
        self.__personagem = personagem

    def valor_total_carta(self) -> int:
        return (
                self.__personagem.energia +
                self.__personagem.habilidade +
                self.__personagem.velocidade +
                self.__personagem.resistencia
        )

    @property
    def personagem(self) -> Personagem:
        return self.__personagem

    @personagem.setter
    def personagem(self, personagem: Personagem):
        if isinstance(personagem, Personagem):
            self.__personagem = personagem