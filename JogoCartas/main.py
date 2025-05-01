from JogoCartas.ControladorJogo import ControladorJogo
from modelos.Personagem import Personagem
from modelos.Carta import Carta
from modelos.Mesa import Mesa
from modelos.Jogador import Jogador
from abstratos.AbstractPersonagem import Tipo


def main():
    # Criando os personagens com os tipos corretos
    personagem1 = Personagem(energia=50, habilidade=40, velocidade=60, resistencia=30, tipo=Tipo.agua)
    personagem2 = Personagem(energia=70, habilidade=50, velocidade=40, resistencia=60, tipo=Tipo.fogo)

    # Criando as cartas
    carta1 = Carta(personagem1)
    carta2 = Carta(personagem2)

    # Criando os jogadores
    jogador1 = Jogador(nome="Jogador 1")
    jogador2 = Jogador(nome="Jogador 2")

    # Incluindo as cartas nas mãos dos jogadores
    jogador1.inclui_carta_na_mao(carta1)
    jogador2.inclui_carta_na_mao(carta2)

    # Criando a mesa
    mesa = Mesa(jogador1=jogador1, jogador2=jogador2, carta_jogador1=carta1, carta_jogador2=carta2)

    # Criando o controlador do jogo
    controlador = ControladorJogo()

    # Simulando a jogada
    vencedor = controlador.jogada(mesa)

    if vencedor:
        print(f"O vencedor da rodada é {vencedor.nome}")
    else:
        print("A rodada terminou em empate!")


if __name__ == "__main__":
    main()
