from constantes import *
import motor_grafico as motor

def desenha_tela(janela, estado, altura_tela, largura_tela):
    motor.preenche_fundo(janela, PRETO)
    motor.desenha_string(janela, (largura_tela-len(estado['mapa'][0]))//2,(altura_tela-len(estado['mapa']))//2 , 'SEU PEAO NÃO CONSEGUIU DERROTAR O REI', BRANCO, PRETO)
    motor.desenha_string(janela, (largura_tela-len(estado['mapa'][0]))//2,(altura_tela-len(estado['mapa']))//2 + 1, 'TENTE NOVAMENTE!!', BRANCO, PRETO)
    motor.mostra_janela(janela)
def atualiza_estado(estado, tecla_apertada):
    if tecla_apertada == motor.ESCAPE or tecla_apertada == 'q':
        estado['tela_atual'] = SAIR
