from random import randint, seed

from constantes import * 

paredes = [
            [0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[10,0],[11,0],[12,0],[13,0],[14,0],[15,0],[16,0],[17,0],[18,0],[19,0],[20,0],[21,0],[22,0],[23,0],[24,0],[25,0],[26,0],[27,0],[28,0],[29,0],[30,0],[31,0],[32,0],[33,0],[34,0],[35,0],[36,0],[37,0],[38,0],[39,0],[40,0],[41,0],[42,0],[43,0],[44,0],[45,0],[46,0],[47,0],[48,0],[49,0],[50,0],[51,0],[52,0],[53,0],[54,0],[55,0],[56,0],[57,0],[58,0],[59,0],[60,0],[61,0],[62,0],[63,0],[64,0],[65,0],[66,0],[67,0],[68,0],[69,0],
            [0,25],[1,25],[2,25],[3,25],[4,25],[5,25],[6,25],[7,25],[8,25],[9,25],[10,25],[11,25],[12,25],[13,25],[14,25],[15,25],[16,25],[17,25],[18,25],[19,25],[20,25],[21,25],[22,25],[23,25],[24,25],[25,25],[26,25],[27,25],[28,25],[29,25],[30,25],[31,25],[32,25],[33,25],[34,25],[35,25],[36,25],[37,25],[38,25],[39,25],[40,25],[41,25],[42,25],[43,25],[44,25],[45,25],[46,25],[47,25],[48,25],[49,25],[50,25],[51,25],[52,25],[53,25],[54,25],[55,25],[56,25],[57,25],[58,25],[59,25],[60,25],[61,25],[62,25],[63,25],[64,25],[65,25],[66,25],[67,25],[68,25],[69,25],
            [0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[0,8],[0,9],[0,10],[0,11],[0,12],[0,13],[0,14],[0,15],[0,16],[0,17],[0,18],[0,19],[0,20],[0,21],[0,22],[0,23],[0,24],
            [70,0],[70,1],[70,2],[70,3],[70,4],[70,5],[70,6],[70,7],[70,8],[70,9],[70,10],[70,11],[70,12],[70,13],[70,14],[70,15],[70,16],[70,17],[70,18],[70,19],[70,20],[70,21],[70,22],[70,23],[70,24],[70,25],
            [0,5],[1,5],[2,5],[3,5],[4,5],[5,5],[6,5],[7,5],[8,5],[9,5],[10,5],[11,5],[12,5],[13,5],[14,5],[15,5],[16,5],[17,5],[18,5],[19,5],[20,5],[21,5],[22,5],[23,5],[24,5],[25,5],[26,5],[27,5],[28,5],[29,5],[30,5],[31,5],[32,5],[33,5],[34,5],[35,5],[36,5],[37,5],[38,5],[39,5],[40,5],[41,5],[42,5],[43,5],[44,5],[45,5],[46,5],[47,5],[48,5],[49,5],[50,5],[51,5],[52,5],[53,5],[54,5],[55,5],[56,5],[57,5],[58,5],[59,5],[60,5],
            [0,19],[1,19],[2,19],[3,19],[4,19],[5,19],[6,19],[7,19],[8,19],[9,19],[10,19],[11,19],[12,19],[13,19],[14,19],[15,19],[16,19],[17,19],[18,19],[19,19],[20,19],[21,19],[22,19],[23,19],[24,19],[25,19],[26,19],[27,19],[28,19],[29,19],[30,19],[31,19],[32,19],[33,19],[34,19],[35,19],[36,19],[37,19],[38,19],[39,19],[40,19],[41,19],[42,19],[43,19],[44,19],[45,19],[46,19],[47,19],[48,19],[49,19],[50,19],[51,19],[52,19],[53,19],[54,19],[55,19],[56,19],[57,19],[58,19],[59,19],[60,19],
            [10,12],[11,12],[12,12],[13,12],[14,12],[15,12],[16,12],[17,12],[18,12],[19,12],[20,12],[21,12],[22,12],[23,12],[24,12],[25,12],[26,12],[27,12],[28,12],[29,12],[30,12],[31,12],[32,12],[33,12],[34,12],[35,12],[36,12],[37,12],[38,12],[39,12],[40,12],[41,12],[42,12],[43,12],[44,12],[45,12],[46,12],[47,12],[48,12],[49,12],[50,12],[51,12],[52,12],[53,12],[54,12],[55,12],[56,12],[57,12],[58,12],[59,12],[60,12],[61,12],[62,12],[63,12],[64,12],[65,12],[66,12],[67,12],[68,12],[69,12],[70,12]
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
            for posicao in paredes:
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
    objetos += gera_objetos(384, PAREDE, MARROM_MAIS_ESCURO, largura_mapa, altura_mapa, posicoes_ocupadas)
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