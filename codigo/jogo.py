import motor_grafico
import tela_inventario
import tela_jogo
from constantes import SAIR, TELA_INVENTARIO, TELA_JOGO, GAME_OVER, INICIO, TETA_TUTORIAL
from inicializacao import inicializa_estado


def jogo(janela, altura_tela, largura_tela):
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
        if estado['tela_atual'] == TETA_TUTORIAL:
            tela_inventario.desenha_tela(janela, estado, altura_tela, largura_tela)
            tecla_apertada = motor_grafico.pega_tecla_apertada(janela)
            tela_inventario.atualiza_estado(estado, tecla_apertada)
        
motor_grafico.chama_funcao_jogo(jogo)