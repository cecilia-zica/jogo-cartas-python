from abstratos.AbstractControladorJogo import *
from modelos.Personagem import Personagem
from modelos.Carta import Carta
from modelos.Mesa import Mesa

class ControladorJogo(AbstractControladorJogo):
    def __init__(self):
        self.__personagems = []
        self.__baralho = []

    @property
    def baralho(self) -> list:
        return self.__baralho

    @baralho.setter
    def baralho(self, baralho: list):
        if isinstance(baralho, list):
            self.__baralho = []

    @property
    def personagems(self) -> list:
        return self.__personagems

    @personagems.setter
    def personagems(self, personagems: list):
        if isinstance(personagems, list):
            self.__personagems = []

    def inclui_personagem_na_lista(self,
                                   energia: int,
                                   habilidade: int,
                                   velocidade: int,
                                   resistencia: int,
                                   tipo: Tipo) -> Personagem:
        person = Personagem(energia, habilidade, velocidade, resistencia, tipo)
        self.__personagems.append(person)
        return person

    def inclui_carta_no_baralho(self, personagem: Personagem) -> Carta:
        carta = Carta(personagem)
        self.__baralho.append(carta)
        return carta

    def jogada(self, mesa: Mesa) -> Jogador:
        player1 = mesa.jogador1
        player2 = mesa.jogador2
        cart1 = mesa.carta_jogador1
        cart2 = mesa.carta_jogador2

        valor1 = cart1.valor_total_carta()
        valor2 = cart2.valor_total_carta()

        if valor1 > valor2:
            player1.inclui_carta_na_mao(cart1)
            player1.inclui_carta_na_mao(cart2)
        elif valor2 > valor1:
            player2.inclui_carta_na_mao(cart1)
            player2.inclui_carta_na_mao(cart2)
        else:  # empate
            player1.inclui_carta_na_mao(cart1)
            player2.inclui_carta_na_mao(cart2)

        # Verifica se alguém perdeu
        if not player1.mao:
            return player2
        elif not player2.mao:
            return player1
        return None  # ninguém venceu ainda



