import motor_grafico
import tela_inventario
import tela_jogo
from constantes import SAIR, TELA_INVENTARIO, TELA_JOGO, GAME_OVER, INICIO
from inicializacao import inicializa_estado


def jogo(janela, altura_tela, largura_tela):
    '''
    Esta é a porta de entrada do jogo.
    Você não precisa chamar esta função. Ela será chamada pelo código
    no final deste arquivo.

    A janela é um estrutura de dados que guarda diversas informações
    sobre uma janela do jogo. A princípio você não precisa entender
    o que ela guarda, mas você deverá passar essa janela como argumento
    para as outras funções que recebem uma janela.
    '''
    estado = inicializa_estado()

    while estado['tela_atual'] != SAIR:
        
        if estado['tela_atual'] == INICIO:
            tela_jogo.desenha_tela(janela, estado, altura_tela, largura_tela)
            tecla_apertada = motor_grafico.pega_tecla_apertada(janela)
            tela_jogo.atualiza_estado(estado, tecla_apertada)
        if estado['tela_atual'] == TELA_JOGO:
            tela_jogo.desenha_tela(janela, estado, altura_tela, largura_tela)
            tecla_apertada = motor_grafico.pega_tecla_apertada(janela)
            tela_jogo.atualiza_estado(estado, tecla_apertada)
        if estado['tela_atual'] == TELA_INVENTARIO:
            tela_inventario.desenha_tela(janela, estado, altura_tela, largura_tela)
            tecla_apertada = motor_grafico.pega_tecla_apertada(janela)
            tela_inventario.atualiza_estado(estado, tecla_apertada)
        if estado['tela_atual'] == GAME_OVER:
            tela_inventario.desenha_tela(janela, estado, altura_tela, largura_tela)
            tecla_apertada = motor_grafico.pega_tecla_apertada(janela)
            tela_inventario.atualiza_estado(estado, tecla_apertada)
        


# Não se preocupe, você não precisa entender o que está acontecendo aqui.
# É apenas uma forma de chamar a função jogo() usando a biblioteca curses.
motor_grafico.chama_funcao_jogo(jogo)