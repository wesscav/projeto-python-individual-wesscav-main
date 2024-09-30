from constantes import *  
import motor_grafico as motor  
import random

def desenha_tela(janela, estado, altura_tela, largura_tela):
    
    motor.preenche_fundo(janela, PRETO)

    if estado['tecla'] != ' ':
        x0 = (largura_tela-len(estado['mapa'][0]))//2
        y0 = (altura_tela-len(estado['mapa']))//2
       
        for largura_mapa in range(len(estado['mapa'][0])):
            for altura_mapa in range(len(estado['mapa'])):
                motor.desenha_string(janela, largura_mapa + x0, altura_mapa + y0,' ', VERDE_ESCURO, PRETO)
        for objeto in estado['objetos']:
            motor.desenha_string(janela, objeto['posicao'][0] + x0, objeto['posicao'][1]+ y0, objeto['tipo'], VERDE_ESCURO, objeto['cor'])
            if objeto['tipo'] == PAREDE: 
                motor.desenha_string(janela, objeto['posicao'][0] + x0, objeto['posicao'][1]+ y0, objeto['tipo'], MARROM_MAIS_ESCURO, objeto['cor'])
        motor.desenha_string(janela, estado['pos_jogador'][0] + x0, estado['pos_jogador'][1] + y0, JOGADOR, VERDE_ESCURO, PRETO)

        
        motor.desenha_string(janela, 0, 0, f'{CORACAO_BRANCO} '*estado['max_vidas'], PRETO, BRANCO)   
        motor.desenha_string(janela, 0, 0, f'{CORACAO} '*estado['vidas'], PRETO, VERMELHO)
        
        if estado['nível'] == 1:
            motor.desenha_string(janela, 0, 2, EXPERIENCIA_VAZIA*2, PRETO, PRETO)
            motor.desenha_string(janela, 0, 2, EXPERIENCIA_CHEIA*estado['inimigos_mortos'], PRETO, PRETO)
        if estado['nível'] == 2:
            motor.desenha_string(janela,0 , 2,EXPERIENCIA_VAZIA*3, PRETO, PRETO)
            motor.desenha_string(janela, 0, 2, EXPERIENCIA_CHEIA*estado['experiência'], PRETO, PRETO)
        if estado['nível'] == 3:
            motor.desenha_string(janela, 0, 2,EXPERIENCIA_VAZIA*5, PRETO, PRETO)
            motor.desenha_string(janela, 0, 2, EXPERIENCIA_CHEIA*estado['experiência'], PRETO, PRETO)
        motor.desenha_string(janela, 0, 10, estado['mensagem'], PRETO, BRANCO)
    else:
        motor.desenha_string(janela, (largura_tela-len(estado['mapa'][0]))//2,(altura_tela-len(estado['mapa']))//2 , 'CHESS 2.0', BRANCO, PRETO)
        motor.desenha_string(janela, (largura_tela-len(estado['mapa'][0]))//2,(altura_tela-len(estado['mapa']))//2 + 1, 'ACOMPANHE A ASCENSAO DO PEÃO PARA DERROTAR O REI', BRANCO, PRETO)
        motor.desenha_string(janela, (largura_tela-len(estado['mapa'][0]))//2,(altura_tela-len(estado['mapa']))//2 + 2, 'PARA ACESSAR O TUTORIAL, APERTE "t"', BRANCO, PRETO)
        motor.desenha_string(janela, (largura_tela-len(estado['mapa'][0]))//2,(altura_tela-len(estado['mapa']))//2 + 2, 'APERTE "v" PARA JOGAR', BRANCO, PRETO)
        if estado['tecla'] == 'v':
            pass
        elif estado['tecla'] == 't':
            motor.desenha_string(janela, (largura_tela-len(estado['mapa'][0]))//2,(altura_tela-len(estado['mapa']))//2 , 'BEM VINDO AO TUTORIAL', BRANCO, PRETO)
            motor.desenha_string(janela, (largura_tela-len(estado['mapa'][0]))//2,(altura_tela-len(estado['mapa']))//2 + 1, 'NO MAPA, HÁ CORAÇÕES, ESPINHOS E PEÇAS INIMIGAS', BRANCO, PRETO)
            motor.desenha_string(janela, (largura_tela-len(estado['mapa'][0]))//2,(altura_tela-len(estado['mapa']))//2 + 2, 'AO DERROTAR CADA MONSTRO, GANHA-SE EXPERIÊNCIA', BRANCO, PRETO)
            motor.desenha_string(janela, (largura_tela-len(estado['mapa'][0]))//2,(altura_tela-len(estado['mapa']))//2 + 3, 'QUANTO MAIOR SEU NÍVEL, MAIS FORTE FICA', BRANCO, PRETO)
            motor.desenha_string(janela, (largura_tela-len(estado['mapa'][0]))//2,(altura_tela-len(estado['mapa']))//2 + 4, 'O REI TE ESPERA NO SALÃO PRINCIPAL, DERROTE-O!', BRANCO, PRETO)
    
    
    motor.mostra_janela(janela)

posições_aleatórias = {'cima': 1, 'baixo': 2, 'esquerda': 3, 'direita': 4}

posicao_paredes = [
            [0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[10,0],[11,0],[12,0],[13,0],[14,0],[15,0],[16,0],[17,0],[18,0],[19,0],[20,0],[21,0],[22,0],[23,0],[24,0],[25,0],[26,0],[27,0],[28,0],[29,0],[30,0],[31,0],[32,0],[33,0],[34,0],[35,0],[36,0],[37,0],[38,0],[39,0],[40,0],[41,0],[42,0],[43,0],[44,0],[45,0],[46,0],[47,0],[48,0],[49,0],[50,0],[51,0],[52,0],[53,0],[54,0],[55,0],[56,0],[57,0],[58,0],[59,0],[60,0],[61,0],[62,0],[63,0],[64,0],[65,0],[66,0],[67,0],[68,0],[69,0],
            [0,25],[1,25],[2,25],[3,25],[4,25],[5,25],[6,25],[7,25],[8,25],[9,25],[10,25],[11,25],[12,25],[13,25],[14,25],[15,25],[16,25],[17,25],[18,25],[19,25],[20,25],[21,25],[22,25],[23,25],[24,25],[25,25],[26,25],[27,25],[28,25],[29,25],[30,25],[31,25],[32,25],[33,25],[34,25],[35,25],[36,25],[37,25],[38,25],[39,25],[40,25],[41,25],[42,25],[43,25],[44,25],[45,25],[46,25],[47,25],[48,25],[49,25],[50,25],[51,25],[52,25],[53,25],[54,25],[55,25],[56,25],[57,25],[58,25],[59,25],[60,25],[61,25],[62,25],[63,25],[64,25],[65,25],[66,25],[67,25],[68,25],[69,25],
            [0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[0,8],[0,9],[0,10],[0,11],[0,12],[0,13],[0,14],[0,15],[0,16],[0,17],[0,18],[0,19],[0,20],[0,21],[0,22],[0,23],[0,24],
            [70,0],[70,1],[70,2],[70,3],[70,4],[70,5],[70,6],[70,7],[70,8],[70,9],[70,10],[70,11],[70,12],[70,13],[70,14],[70,15],[70,16],[70,17],[70,18],[70,19],[70,20],[70,21],[70,22],[70,23],[70,24],[70,25],
            [0,5],[1,5],[2,5],[3,5],[4,5],[5,5],[6,5],[7,5],[8,5],[9,5],[10,5],[11,5],[12,5],[13,5],[14,5],[15,5],[16,5],[17,5],[18,5],[19,5],[20,5],[21,5],[22,5],[23,5],[24,5],[25,5],[26,5],[27,5],[28,5],[29,5],[30,5],[31,5],[32,5],[33,5],[34,5],[35,5],[36,5],[37,5],[38,5],[39,5],[40,5],[41,5],[42,5],[43,5],[44,5],[45,5],[46,5],[47,5],[48,5],[49,5],[50,5],[51,5],[52,5],[53,5],[54,5],[55,5],[56,5],[57,5],[58,5],[59,5],[60,5],
            [0,19],[1,19],[2,19],[3,19],[4,19],[5,19],[6,19],[7,19],[8,19],[9,19],[10,19],[11,19],[12,19],[13,19],[14,19],[15,19],[16,19],[17,19],[18,19],[19,19],[20,19],[21,19],[22,19],[23,19],[24,19],[25,19],[26,19],[27,19],[28,19],[29,19],[30,19],[31,19],[32,19],[33,19],[34,19],[35,19],[36,19],[37,19],[38,19],[39,19],[40,19],[41,19],[42,19],[43,19],[44,19],[45,19],[46,19],[47,19],[48,19],[49,19],[50,19],[51,19],[52,19],[53,19],[54,19],[55,19],[56,19],[57,19],[58,19],[59,19],[60,19],
            [10,12],[11,12],[12,12],[13,12],[14,12],[15,12],[16,12],[17,12],[18,12],[19,12],[20,12],[21,12],[22,12],[23,12],[24,12],[25,12],[26,12],[27,12],[28,12],[29,12],[30,12],[31,12],[32,12],[33,12],[34,12],[35,12],[36,12],[37,12],[38,12],[39,12],[40,12],[41,12],[42,12],[43,12],[44,12],[45,12],[46,12],[47,12],[48,12],[49,12],[50,12],[51,12],[52,12],[53,12],[54,12],[55,12],[56,12],[57,12],[58,12],[59,12],[60,12],[61,12],[62,12],[63,12],[64,12],[65,12],[66,12],[67,12],[68,12],[69,12],[70,12]
    ]
    

def posição_futura_jogador(estado, tecla):
    
    #posicao futura é a posicao que o jogador estará no futuro, usada para saber se a posicao futura será proibida ou nao.
    posicao_futura = estado['pos_jogador'][:]
    if tecla == 'ESQUERDA' and estado['pos_jogador'][0] > 0:
        posicao_futura[0] -= 1
        if posicao_futura in posicao_paredes:
            posicao_futura[0] += 1
            estado['mensagem'] = 'PAREDE!!'
    elif tecla == "DIREITA" and estado['pos_jogador'][0] < 70:
        posicao_futura[0] += 1
        if posicao_futura in posicao_paredes:
            posicao_futura[0] -= 1
            estado['mensagem'] = 'PAREDE!!'
    elif tecla == "CIMA" and estado['pos_jogador'][1] > 0:
        posicao_futura[1] -= 1
        if posicao_futura in posicao_paredes:
            posicao_futura[1] += 1
            estado['mensagem'] = 'PAREDE!!'
    elif tecla == "BAIXO" and estado['pos_jogador'][1] < 25:
        posicao_futura[1] += 1
        if posicao_futura in posicao_paredes:
            posicao_futura[1] -= 1
            estado['mensagem'] = 'PAREDE!!'
        
    return posicao_futura

def atualiza_estado(estado, tecla):
    
    estado['tecla'] = tecla
    estado['mensagem'] = ''
    bateu_monstro = False
    if estado['vidas'] > 0:
        posição_jogador = posição_futura_jogador(estado, tecla)
    else:
        posição_jogador = [0,0]

    #nível e experiência:
    if estado['experiência'] == 2 and estado['nível'] == 1:
        estado['nível'] += 1
        estado['mensagem'] = 'Você atingiu o Nível 2'
        estado['experiência'] = 0
        estado['vidas'] = 5

    elif estado['experiência'] == 3 and estado['nível'] == 2:
        estado['nível'] += 1
        estado['mensagem'] = 'Você atingiu o Nível 3'
        estado['experiência'] = 0
        estado['vidas'] = 5
    
    elif estado['experiência'] == 5 and estado['nível'] == 3:
        estado['nível'] += 1
        estado['mensagem'] = 'Você atingiu o Nível MÁXIMO'
        estado['experiência'] = 0
        estado['vidas'] = 5

    if tecla == 'i':
        estado['tela_atual'] = TELA_INVENTARIO
    # Termina o jogo se o jogador apertar ESC ou 'q'
    if tecla == motor.ESCAPE or tecla =='q':
        estado['tela_atual'] = SAIR
    if estado['vidas'] <= 0:
        estado['mensagem'] = 'Você morreu, tente novamente!! Aperte ESC para jogar novamente!'

    #análise jogo para objetos!!
    posição_futura = posição_futura_jogador(estado, tecla)

    for objeto in estado['objetos']:
        if objeto['tipo'] == ESPINHO:
            if objeto['posicao'] == posição_futura:
                estado['vidas'] -= 1
                estado['mensagem'] = 'O espinho te engoliu, saia!!'

        elif objeto['tipo'] == CORACAO:
            if objeto['posicao'] == posição_futura:
                estado['objetos'].remove(objeto)
                if estado['vidas'] == estado['max_vidas']:
                    estado['mensagem'] = 'Você chegou na vida máxima!'
                if estado['vidas'] < estado['max_vidas']:
                    estado['vidas'] += 1
                    
        elif objeto['tipo'] == MONSTRO:
            if estado['vidas'] > 0:
                    
                posicao_futura_mostro = objeto['posicao'][:]
                direção = random.randint(1,4)
                if posições_aleatórias['baixo'] == direção and objeto['posicao'][1] < 23:
                    posicao_futura_mostro[1] += 1
                    if posicao_futura_mostro in posicao_paredes or posicao_futura_mostro in estado['posicoes_ocupadas']:
                        posicao_futura_mostro[1] -= 1

                elif posições_aleatórias['cima'] == direção and objeto['posicao'][1] > 2:
                    posicao_futura_mostro[1] -= 1
                    if posicao_futura_mostro in posicao_paredes or posicao_futura_mostro in estado['posicoes_ocupadas']:
                        posicao_futura_mostro[1] += 1

                elif posições_aleatórias['direita'] == direção and objeto['posicao'][0] < 68:
                    posicao_futura_mostro[0] += 1
                    if posicao_futura_mostro in posicao_paredes or posicao_futura_mostro in estado['posicoes_ocupadas']:
                        posicao_futura_mostro[0] -= 1

                elif posições_aleatórias['esquerda'] == direção and objeto['posicao'][0] > 2 and objeto['posicao']:
                    posicao_futura_mostro[0] -= 1
                    if posicao_futura_mostro in posicao_paredes or posicao_futura_mostro in estado['posicoes_ocupadas']:
                        posicao_futura_mostro[0] += 1

                objeto['posicao'] = posicao_futura_mostro
                
                if posição_jogador == posicao_futura_mostro or posição_jogador == objeto["posicao"]:
                    bateu_monstro = True
                
                if objeto['posicao'] == estado['pos_jogador']:
                    probabilidade_de_ataque = random.randint(0,100)
                    if probabilidade_de_ataque <= objeto['probabilidade_de_ataque']:
                        estado['vidas'] -= 1
                        estado['mensagem'] = 'Você perdeu uma vida!'

                    else:
                        objeto['vida'] -= 1
                        vida_monstro = objeto['vida']
                        estado['mensagem'] = f'O monstro perdeu uma vida! Ele tem {vida_monstro} vida(s)!'
                        if objeto['vida'] <= 0:
                            estado['mensagem'] = 'Você derrotou DAMA!'
                            estado['objetos'].remove(objeto)
                            estado['inimigos_mortos'] += 1
                            estado['experiência'] += 1

            if estado['nível'] == 2:
                objeto['probabilidade_de_ataque'] = 30
                
            if estado['nível'] == 3:
                objeto['probabilidade_de_ataque'] = 25
                
            if estado['nível'] == 4:
                objeto['probabilidade_de_ataque'] = 15
                
                            
        elif objeto['tipo'] == MONSTRO2:
            if estado['vidas'] > 0:
                posicao_futura_mostro = objeto['posicao'][:]
                direção = random.randint(1,4)
                if posições_aleatórias['baixo'] == direção:
                    posicao_futura_mostro[1] += 1
                    if posicao_futura_mostro in posicao_paredes or posicao_futura_mostro in estado['posicoes_ocupadas']:
                        posicao_futura_mostro[1] -= 1

                elif posições_aleatórias['cima'] == direção:
                    posicao_futura_mostro[1] -= 1
                    if posicao_futura_mostro in posicao_paredes or posicao_futura_mostro in estado['posicoes_ocupadas']:
                        posicao_futura_mostro[1] += 1
                elif posições_aleatórias['direita'] == direção:
                    posicao_futura_mostro[0] += 1
                    if posicao_futura_mostro in posicao_paredes or posicao_futura_mostro in estado['posicoes_ocupadas']:
                        posicao_futura_mostro[0] -= 1
                elif posições_aleatórias['esquerda'] == direção:
                    posicao_futura_mostro[0] -= 1
                    if posicao_futura_mostro in posicao_paredes or posicao_futura_mostro in estado['posicoes_ocupadas']:
                        posicao_futura_mostro[0] += 1

                objeto['posicao'] = posicao_futura_mostro
                if posição_jogador == posicao_futura_mostro or posição_jogador == objeto["posicao"]:
                    bateu_monstro = True
                
                if objeto['posicao'] == estado['pos_jogador']:
                    probabilidade_de_ataque = random.randint(0,100)
                    if probabilidade_de_ataque <= objeto['probabilidade_de_ataque']:
                        estado['vidas'] -= 1
                        estado['mensagem'] = 'Você perdeu uma vida!'

                    else:
                        objeto['vida'] -= 1
                        vida_monstro = objeto['vida']
                        estado['mensagem'] = f'O monstro perdeu uma vida! Ele tem {vida_monstro} vida(s)!'
                        if objeto['vida'] <= 0:
                            estado['mensagem'] = 'Você derrotou CAVALO!'
                            estado['objetos'].remove(objeto)
                            estado['inimigos_mortos'] += 1
                            estado['experiência'] += 1  

            if estado['nível'] == 2:
                objeto['probabilidade_de_ataque'] = 45
            
            if estado['nível'] == 3:
                objeto['probabilidade_de_ataque'] = 25
            
            if estado['nível'] == 4:
                objeto['probabilidade_de_ataque'] = 20

    if not bateu_monstro:
        estado['pos_jogador'] = posição_jogador