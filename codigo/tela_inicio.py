from constantes import *
import motor_grafico as motor


def desenha_tela(janela, estado, altura_tela, largura_tela):
    motor.preenche_fundo(janela, PRETO)
    motor.desenha_string(janela, (largura_tela-len(estado['mapa'][0]))//2,(altura_tela-len(estado['mapa']))//2 , 'CHESS 2.0', BRANCO, PRETO)
    motor.desenha_string(janela, (largura_tela-len(estado['mapa'][0]))//2,(altura_tela-len(estado['mapa']))//2 + 1, 'ACOMPANHE A ASCENSAO DO PEÃO PARA DERROTAR O REI', BRANCO, PRETO)
    motor.desenha_string(janela, (largura_tela-len(estado['mapa'][0]))//2,(altura_tela-len(estado['mapa']))//2 + 2, 'PARA ACESSAR O TUTORIAL, APERTE "t"', BRANCO, PRETO)
    motor.desenha_string(janela, (largura_tela-len(estado['mapa'][0]))//2,(altura_tela-len(estado['mapa']))//2 + 2, 'APERTE "v" PARA JOGAR', BRANCO, PRETO)
    motor.mostra_janela(janela)
def atualiza_estado(estado, tecla_apertada):
    if tecla_apertada == 't':
        estado['tela_atual'] = TETA_TUTORIAL
    if tecla_apertada == motor.ESCAPE or tecla_apertada == 'q':
        estado['tela_atual'] = SAIR
    if tecla_apertada == 'v':
        estado['tela_atual'] = TELA_JOGO

