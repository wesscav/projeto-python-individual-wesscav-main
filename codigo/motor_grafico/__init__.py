from .constantes_do_motor import *
MOTOR = 'curses'


if MOTOR == 'curses':
    from . import motor_curses as motor
elif MOTOR == 'pygame':
    from . import motor_pygame as motor
else:
    raise ImportError('Motor gráfico não encontrado')


def chama_funcao_jogo(funcao):
    motor.chama_funcao_jogo(funcao)


def pega_tecla_apertada(janela):
    return motor.pega_tecla_apertada(janela)


def preenche_fundo(janela, cor_rgb):
    motor.preenche_fundo(janela, cor_rgb)


def desenha_string(janela, x, y, string, cor_fundo, cor_texto):
    motor.desenha_string(janela, x, y, string, cor_fundo, cor_texto)


def mostra_janela(janela):
    motor.mostra_janela(janela)
