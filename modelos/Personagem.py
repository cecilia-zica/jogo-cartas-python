from abstratos.AbstractPersonagem import *


class Personagem(AbstractPersonagem):
    #Construtor fornecido, nao deve ser alterado
    def __init__(self, energia: int, habilidade: int,
                 velocidade: int, resistencia: int, tipo: Tipo):
        self.__energia = energia
        self.__habilidade = habilidade
        self.__velocidade = velocidade
        self.__resistencia = resistencia
        self.__tipo = tipo

    @property
    def tipo(self) -> Tipo:
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo: Tipo):
        if isinstance(tipo, Tipo):
            self.__tipo = tipo

    @property
    def energia(self) -> int:
        return self.__energia

    @energia.setter
    def energia(self, energia: int):
        if isinstance(energia, int):
            self.__energia = energia

    @property
    def habilidade(self) -> int:
        return self.__habilidade

    @habilidade.setter
    def habilidade(self, habilidade:int):
        if isinstance(habilidade, int):
            self.__habilidade = habilidade

    @property
    def velocidade(self) -> int:
        return self.__velocidade

    @velocidade.setter
    def velocidade(self, velocidade: int):
        if isinstance(velocidade, int):
            self.__velocidade = velocidade
    @property
    def resistencia(self) -> int:
        return self.__resistencia

    @resistencia.setter
    def resistencia(self, resistencia: int):
        if isinstance(resistencia, int):
            self.__resistencia = resistencia
