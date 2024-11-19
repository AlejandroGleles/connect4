import numpy as np
import random
import pygame
import sys
import math
import time

# Cores
AZUL = (0, 0, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
AMARELO = (255, 255, 0)

# Configurações do Tabuleiro
LINHAS = 7
COLUNAS = 8
TAMANHO_JANELA = 4  # Mudando para 4, já que estamos buscando vitórias de 4 peças consecutivas

# Identificadores do jogador e IA
JOGADOR = 0
IA = 1
VAZIO = 0
PECA_JOGADOR = 1
PECA_IA = 2

# Variáveis globais para contar os nós expandidos
nós_expandidos = 0

def criar_tabuleiro():
    """Cria um tabuleiro vazio de 7x8 (linhas x colunas)"""
    return np.zeros((LINHAS, COLUNAS))

def colocar_peca(tabuleiro, linha, coluna, peca):
    """Coloca uma peça no tabuleiro na posição especificada"""
    tabuleiro[linha][coluna] = peca

def localização_valida(tabuleiro, coluna):
    """Verifica se a coluna está cheia ou não"""
    return tabuleiro[LINHAS-1][coluna] == 0

def próxima_linha_aberta(tabuleiro, coluna):
    """Retorna a próxima linha disponível para uma peça na coluna especificada"""
    for r in range(LINHAS):
        if tabuleiro[r][coluna] == 0:
            return r

def movimento_vencedor(tabuleiro, peca):
    """Verifica se houve uma vitória com a peça fornecida (IA ou jogador)"""
    # Verifica linhas, colunas e diagonais para uma vitória
    for c in range(COLUNAS-3):
        for r in range(LINHAS):
            if all(tabuleiro[r][c+i] == peca for i in range(4)):
                return True
    for c in range(COLUNAS):
        for r in range(LINHAS-3):
            if all(tabuleiro[r+i][c] == peca for i in range(4)):
                return True
    for c in range(COLUNAS-3):
        for r in range(LINHAS-3):
            if all(tabuleiro[r+i][c+i] == peca for i in range(4)):
                return True
    for c in range(COLUNAS-3):
        for r in range(3, LINHAS):
            if all(tabuleiro[r-i][c+i] == peca for i in range(4)):
                return True
    return False

def avaliar_janela(janela, peca):
    """Avalia uma janela de 4 posições e retorna um score com base na posição"""
    score = 0
    peca_oponente = PECA_JOGADOR if peca == PECA_IA else PECA_IA

    # Vantagens para a IA
    if janela.count(peca) == 4:
        score += 100  # Vitória da IA
    elif janela.count(peca) == 3 and janela.count(VAZIO) == 1:
        score += 10  # A IA pode ganhar na próxima jogada
    elif janela.count(peca) == 2 and janela.count(VAZIO) == 2:
        score += 5  # A IA está perto de ganhar

    # Desvantagens para o Jogador (prevenir vitória)
    if janela.count(peca_oponente) == 3 and janela.count(VAZIO) == 1:
        score -= 50  # Impede que o jogador ganhe
    elif janela.count(peca_oponente) == 2 and janela.count(VAZIO) == 2:
        score -= 10  # Prevenção de um possível alinhamento do jogador
    
    return score

def pontuar_posição(tabuleiro, peca):
    """Calcula o score global do tabuleiro para uma peça"""
    score = 0
    centro_array = [int(i) for i in list(tabuleiro[:, COLUNAS//2])]
    centro_count = centro_array.count(peca)
    score += centro_count * 3  # A centralidade das peças é mais importante

    # Análise das linhas, colunas e diagonais
    for r in range(LINHAS):
        linha_array = [int(i) for i in list(tabuleiro[r, :])]
        for c in range(COLUNAS-3):
            janela = linha_array[c:c+TAMANHO_JANELA]
            score += avaliar_janela(janela, peca)

    for c in range(COLUNAS):
        coluna_array = [int(i) for i in list(tabuleiro[:, c])]
        for r in range(LINHAS-3):
            janela = coluna_array[r:r+TAMANHO_JANELA]
            score += avaliar_janela(janela, peca)

    for r in range(LINHAS-3):
        for c in range(COLUNAS-3):
            janela = [tabuleiro[r+i][c+i] for i in range(TAMANHO_JANELA)]
            score += avaliar_janela(janela, peca)
    for r in range(LINHAS-3):
        for c in range(COLUNAS-3):
            janela = [tabuleiro[r+3-i][c+i] for i in range(TAMANHO_JANELA)]
            score += avaliar_janela(janela, peca)
    
    return score

def é_nó_terminal(tabuleiro):
    """Verifica se o jogo acabou (vitória ou empate)"""
    return movimento_vencedor(tabuleiro, PECA_JOGADOR) or movimento_vencedor(tabuleiro, PECA_IA) or len(obter_localizações_validas(tabuleiro)) == 0

def minimax(tabuleiro, profundidade, alpha, beta, jogador_maximizador):
    """Algoritmo Minimax com poda Alfa-Beta"""
    global nós_expandidos
    nós_expandidos += 1
    localizações_validas = obter_localizações_validas(tabuleiro)
    é_terminal = é_nó_terminal(tabuleiro)
    
    if profundidade == 0 or é_terminal:
        if é_terminal:
            if movimento_vencedor(tabuleiro, PECA_IA):
                return (None, 100000000000000)
            elif movimento_vencedor(tabuleiro, PECA_JOGADOR):
                return (None, -10000000000000)
            else:
                return (None, 0)
        else:
            return (None, pontuar_posição(tabuleiro, PECA_IA))

    if jogador_maximizador:
        valor = -math.inf
        coluna = random.choice(localizações_validas)
        for col in localizações_validas:
            linha = próxima_linha_aberta(tabuleiro, col)
            tabuleiro_copia = tabuleiro.copy()
            colocar_peca(tabuleiro_copia, linha, col, PECA_IA)
            novo_score = minimax(tabuleiro_copia, profundidade-1, alpha, beta, False)[1]
            if novo_score > valor:
                valor = novo_score
                coluna = col
            alpha = max(alpha, valor)
            if alpha >= beta:
                break
        return coluna, valor
    else:
        valor = math.inf
        coluna = random.choice(localizações_validas)
        for col in localizações_validas:
            linha = próxima_linha_aberta(tabuleiro, col)
            tabuleiro_copia = tabuleiro.copy()
            colocar_peca(tabuleiro_copia, linha, col, PECA_JOGADOR)
            novo_score = minimax(tabuleiro_copia, profundidade-1, alpha, beta, True)[1]
            if novo_score < valor:
                valor = novo_score
                coluna = col
            beta = min(beta, valor)
            if alpha >= beta:
                break
        return coluna, valor

def obter_localizações_validas(tabuleiro):
    """Retorna uma lista com as colunas válidas onde a peça pode ser colocada"""
    return [col for col in range(COLUNAS) if localização_valida(tabuleiro, col)]

def desenhar_tabuleiro(tabuleiro, tela, TAMANHO_QUADRADO, RAIO, altura):
    """Desenha o tabuleiro na tela usando Pygame"""
    for c in range(COLUNAS):
        for r in range(LINHAS):
            pygame.draw.rect(tela, AZUL, (c*TAMANHO_QUADRADO, r*TAMANHO_QUADRADO+TAMANHO_QUADRADO, TAMANHO_QUADRADO, TAMANHO_QUADRADO))
            pygame.draw.circle(tela, PRETO, (int(c*TAMANHO_QUADRADO+TAMANHO_QUADRADO/2), int(r*TAMANHO_QUADRADO+TAMANHO_QUADRADO+TAMANHO_QUADRADO/2)), RAIO)

    for c in range(COLUNAS):
        for r in range(LINHAS):
            if tabuleiro[r][c] == PECA_JOGADOR:
                pygame.draw.circle(tela, VERMELHO, (int(c*TAMANHO_QUADRADO+TAMANHO_QUADRADO/2), altura-int(r*TAMANHO_QUADRADO+TAMANHO_QUADRADO/2)), RAIO)
            elif tabuleiro[r][c] == PECA_IA:
                pygame.draw.circle(tela, AMARELO, (int(c*TAMANHO_QUADRADO+TAMANHO_QUADRADO/2), altura-int(r*TAMANHO_QUADRADO+TAMANHO_QUADRADO/2)), RAIO)
    pygame.display.update()

def imprimir_mensagem_fim_de_jogo(vencedor, tempo_ia):
    """Imprime a mensagem de fim de jogo no terminal"""
    if vencedor == JOGADOR:
        print("O Jogador 1 venceu!!")
    elif vencedor == IA:
        print("A IA venceu!!")
    else:
        print("Empate!")
    print(f"Tempo gasto pela IA: {tempo_ia} segundos")
    print(f"Nós expandidos: {nós_expandidos}")

def principal():
    tabuleiro = criar_tabuleiro()
    jogo_acabado = False
    profundidade = int(input("Escolha a profundidade (número de níveis desejados): "))
    algoritmo = input("Escolha o algoritmo (minimax / alpha_beta): ").lower()
    pygame.init()

    TAMANHO_QUADRADO = 90
    largura = COLUNAS * TAMANHO_QUADRADO
    altura = (LINHAS + 1) * TAMANHO_QUADRADO
    tamanho = (largura, altura)
    tela = pygame.display.set_mode(tamanho)

    RAIO = int(TAMANHO_QUADRADO/2 - 5)
    distancia = 50
    font = pygame.font.SysFont("monospace", 75)

    # Exibe o tabuleiro vazio inicialmente
    desenhar_tabuleiro(tabuleiro, tela, TAMANHO_QUADRADO, RAIO, altura)

    # Decide aleatoriamente quem começa
    quem_comeca = random.choice([JOGADOR, IA])

    while not jogo_acabado:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEMOTION:
                pass
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:  # Botão esquerdo do mouse
                    x_pos = evento.pos[0]
                    coluna = x_pos // TAMANHO_QUADRADO
                    if localização_valida(tabuleiro, coluna):
                        linha = próxima_linha_aberta(tabuleiro, coluna)
                        colocar_peca(tabuleiro, linha, coluna, PECA_JOGADOR)
                        desenhar_tabuleiro(tabuleiro, tela, TAMANHO_QUADRADO, RAIO, altura)

                        if movimento_vencedor(tabuleiro, PECA_JOGADOR):
                            jogo_acabado = True
                            vencedor = JOGADOR
                            imprimir_mensagem_fim_de_jogo(vencedor, 3.0)
                            break

                        # IA faz sua jogada
                        print("A IA está pensando...")
                        time.sleep(1)  # Delay de 1 segundo para a IA pensar

                        coluna_ia, _ = minimax(tabuleiro, profundidade, -math.inf, math.inf, True)
                        linha_ia = próxima_linha_aberta(tabuleiro, coluna_ia)
                        colocar_peca(tabuleiro, linha_ia, coluna_ia, PECA_IA)
                        desenhar_tabuleiro(tabuleiro, tela, TAMANHO_QUADRADO, RAIO, altura)

                        if movimento_vencedor(tabuleiro, PECA_IA):
                            jogo_acabado = True
                            vencedor = IA
                            imprimir_mensagem_fim_de_jogo(vencedor, 3.0)
                            break

        pygame.display.update()

if __name__ == "__main__":
    principal()
