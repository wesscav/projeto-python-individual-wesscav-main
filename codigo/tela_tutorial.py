from constantes import *
import motor_grafico as motor


def desenha_tela(janela, estado, altura_tela, largura_tela):
    motor.preenche_fundo(janela, PRETO)
    motor.desenha_string(janela, (largura_tela-len(estado['mapa'][0]))//2,(altura_tela-len(estado['mapa']))//2 , 'BEM VINDO AO TUTORIAL', BRANCO, PRETO)
    motor.desenha_string(janela, (largura_tela-len(estado['mapa'][0]))//2,(altura_tela-len(estado['mapa']))//2 + 1, 'NO MAPA, HÁ CORAÇÕES, ESPINHOS E PEÇAS INIMIGAS', BRANCO, PRETO)
    motor.desenha_string(janela, (largura_tela-len(estado['mapa'][0]))//2,(altura_tela-len(estado['mapa']))//2 + 2, 'AO DERROTAR CADA MONSTRO, GANHA-SE EXPERIÊNCIA', BRANCO, PRETO)
    motor.desenha_string(janela, (largura_tela-len(estado['mapa'][0]))//2,(altura_tela-len(estado['mapa']))//2 + 3, 'QUANTO MAIOR SEU NÍVEL, MAIS FORTE FICA', BRANCO, PRETO)
    motor.desenha_string(janela, (largura_tela-len(estado['mapa'][0]))//2,(altura_tela-len(estado['mapa']))//2 + 4, 'O REI TE ESPERA NO SALÃO PRINCIPAL, DERROTE-O!', BRANCO, PRETO)
    motor.mostra_janela(janela)
def atualiza_estado(estado, tecla_apertada):
    if tecla_apertada == motor.ESCAPE or tecla_apertada == 'q':
        estado['tela_atual'] = SAIR
    if tecla_apertada == 'j':
        estado['tela_atual'] = TELA_JOGO