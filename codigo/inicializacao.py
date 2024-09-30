from random import randint, seed

from constantes import * 

paredes = [
            [0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[10,0],[11,0],[12,0],[13,0],[14,0],[15,0],[16,0],[17,0],[18,0],[19,0],[20,0],[21,0],[22,0],[23,0],[24,0],[25,0],[26,0],[27,0],[28,0],[29,0],[30,0],[31,0],[32,0],[33,0],[34,0],[35,0],[36,0],[37,0],[38,0],[39,0],[40,0],[41,0],[42,0],[43,0],[44,0],[45,0],[46,0],[47,0],[48,0],[49,0],[50,0],[51,0],[52,0],[53,0],[54,0],[55,0],[56,0],[57,0],[58,0],[59,0],[60,0],[61,0],[62,0],[63,0],[64,0],[65,0],[66,0],[67,0],[68,0],[69,0],
            [0,25],[1,25],[2,25],[3,25],[4,25],[5,25],[6,25],[7,25],[8,25],[9,25],[10,25],[11,25],[12,25],[13,25],[14,25],[15,25],[16,25],[17,25],[18,25],[19,25],[20,25],[21,25],[22,25],[23,25],[24,25],[25,25],[26,25],[27,25],[28,25],[29,25],[30,25],[31,25],[32,25],[33,25],[34,25],[35,25],[36,25],[37,25],[38,25],[39,25],[40,25],[41,25],[42,25],[43,25],[44,25],[45,25],[46,25],[47,25],[48,25],[49,25],[50,25],[51,25],[52,25],[53,25],[54,25],[55,25],[56,25],[57,25],[58,25],[59,25],[60,25],[61,25],[62,25],[63,25],[64,25],[65,25],[66,25],[67,25],[68,25],[69,25],
            [0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[0,8],[0,9],[0,10],[0,11],[0,12],[0,13],[0,14],[0,15],[0,16],[0,17],[0,18],[0,19],[0,20],[0,21],[0,22],[0,23],[0,24],
            [70,0],[70,1],[70,2],[70,3],[70,4],[70,5],[70,6],[70,7],[70,8],[70,9],[70,10],[70,11],[70,12],[70,13],[70,14],[70,15],[70,16],[70,17],[70,18],[70,19],[70,20],[70,21],[70,22],[70,23],[70,24],[70,25]
    ]

def gera_posicao_desocupada(posicoes_ocupadas, largura_mapa, altura_mapa):
    while True:
        x = randint(1, largura_mapa-2)
        y = randint(1, altura_mapa-2)
        posicao = [x, y]
        if posicao not in posicoes_ocupadas and posicao not in paredes:
            posicoes_ocupadas.append(posicao)
            return posicao

def gera_objetos(quantidade, tipo, cor, largura_mapa, altura_mapa, posicoes_ocupadas):

    posicao = gera_posicao_desocupada(posicoes_ocupadas, largura_mapa, altura_mapa)
    objetos = []
    posicao_paredes = [
            [0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[10,0],[11,0],[12,0],[13,0],[14,0],[15,0],[16,0],[17,0],[18,0],[19,0],[20,0],[21,0],[22,0],[23,0],[24,0],[25,0],[26,0],[27,0],[28,0],[29,0],[30,0],[31,0],[32,0],[33,0],[34,0],[35,0],[36,0],[37,0],[38,0],[39,0],[40,0],[41,0],[42,0],[43,0],[44,0],[45,0],[46,0],[47,0],[48,0],[49,0],[50,0],[51,0],[52,0],[53,0],[54,0],[55,0],[56,0],[57,0],[58,0],[59,0],[60,0],[61,0],[62,0],[63,0],[64,0],[65,0],[66,0],[67,0],[68,0],[69,0],
            [0,25],[1,25],[2,25],[3,25],[4,25],[5,25],[6,25],[7,25],[8,25],[9,25],[10,25],[11,25],[12,25],[13,25],[14,25],[15,25],[16,25],[17,25],[18,25],[19,25],[20,25],[21,25],[22,25],[23,25],[24,25],[25,25],[26,25],[27,25],[28,25],[29,25],[30,25],[31,25],[32,25],[33,25],[34,25],[35,25],[36,25],[37,25],[38,25],[39,25],[40,25],[41,25],[42,25],[43,25],[44,25],[45,25],[46,25],[47,25],[48,25],[49,25],[50,25],[51,25],[52,25],[53,25],[54,25],[55,25],[56,25],[57,25],[58,25],[59,25],[60,25],[61,25],[62,25],[63,25],[64,25],[65,25],[66,25],[67,25],[68,25],[69,25],
            [0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[0,8],[0,9],[0,10],[0,11],[0,12],[0,13],[0,14],[0,15],[0,16],[0,17],[0,18],[0,19],[0,20],[0,21],[0,22],[0,23],[0,24],
            [70,0],[70,1],[70,2],[70,3],[70,4],[70,5],[70,6],[70,7],[70,8],[70,9],[70,10],[70,11],[70,12],[70,13],[70,14],[70,15],[70,16],[70,17],[70,18],[70,19],[70,20],[70,21],[70,22],[70,23],[70,24],[70,25]
    ]
   
    for i in range(quantidade):
        posicao = gera_posicao_desocupada(posicoes_ocupadas, largura_mapa, altura_mapa)
        if tipo == CORACAO:
            objetos.append({
                'tipo': tipo,
                'posicao': posicao,
                'cor': cor,
                })
        if tipo == ESPINHO:
            objetos.append({
                'tipo': tipo,
                'posicao': posicao,
                'cor': cor,
                })
        if tipo == MONSTRO:
            objetos.append({
                'tipo': tipo,
                'posicao': posicao,
                'cor': cor,
                'vida': 3,
                'probabilidade_de_ataque' : 40})
        if tipo == PAREDE:
            for posicao in posicao_paredes:
                objetos.append({
                    'tipo': tipo,
                    'posicao': posicao,
                    'cor': cor,
                    })
        if tipo == MONSTRO2:
            objetos.append({
                'tipo': tipo,
                'posicao': posicao,
                'cor': cor,
                'vida': 2,
                'probabilidade_de_ataque' : 50})

    return objetos


def inicializa_estado():
    #mapa possui 70 de largura e 24 de altura
    mapa = [
        [' '] * 70,
        [' '] * 70,
        [' '] * 70,
        [' '] * 70,
        [' '] * 70,
        [' '] * 70,
        [' '] * 70,
        [' '] * 70,
        [' '] * 70,
        [' '] * 70,
        [' '] * 70,
        [' '] * 70,
        [' '] * 70,
        [' '] * 70,
        [' '] * 70,
        [' '] * 70,
        [' '] * 70,
        [' '] * 70,
        [' '] * 70,
        [' '] * 70,
        [' '] * 70,
        [' '] * 70,
        [' '] * 70,
        [' '] * 70,
        [' '] * 70
    ]
    
    largura_mapa = len(mapa[0])
    altura_mapa = len(mapa)
    
    #posicao inicial jogador
    pos_jogador = [1, 2]  
    
    posicoes_ocupadas = [pos_jogador]
    objetos = []
    objetos += gera_objetos(12, CORACAO, VERMELHO, largura_mapa, altura_mapa, posicoes_ocupadas)
    objetos += gera_objetos(6, ESPINHO, VERDE_CLARO, largura_mapa, altura_mapa, posicoes_ocupadas)
    objetos += gera_objetos(5, MONSTRO, BRANCO, largura_mapa, altura_mapa, posicoes_ocupadas)
    objetos += gera_objetos(189, PAREDE, MARROM_MAIS_ESCURO, largura_mapa, altura_mapa, posicoes_ocupadas)
    objetos += gera_objetos(5, MONSTRO2, BRANCO, largura_mapa, altura_mapa, posicoes_ocupadas)
    
    return {
        'tela_atual': TELA_JOGO,
        'pos_jogador': pos_jogador, 
        'vidas': 5,  
        'max_vidas': 5,  
        'objetos': objetos,
        'mapa': mapa,
        'mensagem': '',
        'experiência': 0,
        'nível': 1,
        'inimigos_mortos': 0  
    }