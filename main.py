import numpy as np
import time

# Dimensões do tabuleiro
ROWS = 6
COLUMNS = 7

def criar_tabuleiro():
    return np.zeros((ROWS, COLUMNS), dtype=int)

def imprimir_tabuleiro(tabuleiro):
    print(np.flip(tabuleiro, 0))

def jogada_valida(tabuleiro, coluna):
    return tabuleiro[ROWS - 1][coluna] == 0

def obter_linha_vazia(tabuleiro, coluna):
    for r in range(ROWS):
        if tabuleiro[r][coluna] == 0:
            return r

def fazer_jogada(tabuleiro, linha, coluna, peca):
    tabuleiro[linha][coluna] = peca

def verificar_vitoria(tabuleiro, peca):
    # Checar vitória horizontal
    for r in range(ROWS):
        for c in range(COLUMNS - 3):
            if all([tabuleiro[r][c + i] == peca for i in range(4)]):
                return True
    # Checar vitória vertical
    for r in range(ROWS - 3):
        for c in range(COLUMNS):
            if all([tabuleiro[r + i][c] == peca for i in range(4)]):
                return True
    # Checar vitória diagonal positiva
    for r in range(ROWS - 3):
        for c in range(COLUMNS - 3):
            if all([tabuleiro[r + i][c + i] == peca for i in range(4)]):
                return True
    # Checar vitória diagonal negativa
    for r in range(3, ROWS):
        for c in range(COLUMNS - 3):
            if all([tabuleiro[r - i][c + i] == peca for i in range(4)]):
                return True
    return False

def avaliacao(tabuleiro, peca):
    # Função de avaliação simples para o estado atual
    oponente = 1 if peca == 2 else 2
    if verificar_vitoria(tabuleiro, peca):
        return 100
    elif verificar_vitoria(tabuleiro, oponente):
        return -100
    else:
        return 0

def movimentos_validos(tabuleiro):
    return [c for c in range(COLUMNS) if jogada_valida(tabuleiro, c)]

def minimax(tabuleiro, profundidade, maximizando, peca, alfa=-np.inf, beta=np.inf):
    movimentos = movimentos_validos(tabuleiro)
    if profundidade == 0 or not movimentos or verificar_vitoria(tabuleiro, 1) or verificar_vitoria(tabuleiro, 2):
        return avaliacao(tabuleiro, peca), None

    if maximizando:
        valor_max = -np.inf
        melhor_coluna = None
        for col in movimentos:
            linha = obter_linha_vazia(tabuleiro, col)
            copia = tabuleiro.copy()
            fazer_jogada(copia, linha, col, peca)
            nova_avaliacao, _ = minimax(copia, profundidade - 1, False, peca, alfa, beta)
            if nova_avaliacao > valor_max:
                valor_max = nova_avaliacao
                melhor_coluna = col
            alfa = max(alfa, valor_max)
            if alfa >= beta:
                break
        return valor_max, melhor_coluna
    else:
        valor_min = np.inf
        melhor_coluna = None
        oponente = 1 if peca == 2 else 2
        for col in movimentos:
            linha = obter_linha_vazia(tabuleiro, col)
            copia = tabuleiro.copy()
            fazer_jogada(copia, linha, col, oponente)
            nova_avaliacao, _ = minimax(copia, profundidade - 1, True, peca, alfa, beta)
            if nova_avaliacao < valor_min:
                valor_min = nova_avaliacao
                melhor_coluna = col
            beta = min(beta, valor_min)
            if alfa >= beta:
                break
        return valor_min, melhor_coluna

# Jogo
def main():
    tabuleiro = criar_tabuleiro()
    fim = False
    turno = 0

    while not fim:
        imprimir_tabuleiro(tabuleiro)
        if turno == 0:
            col = int(input("Jogador 1, escolha uma coluna (0-6): "))
            if jogada_valida(tabuleiro, col):
                linha = obter_linha_vazia(tabuleiro, col)
                fazer_jogada(tabuleiro, linha, col, 1)
                if verificar_vitoria(tabuleiro, 1):
                    imprimir_tabuleiro(tabuleiro)
                    print("Jogador 1 venceu!")
                    fim = True
        else:
            _, col = minimax(tabuleiro, profundidade=3, maximizando=True, peca=2)
            if jogada_valida(tabuleiro, col):
                linha = obter_linha_vazia(tabuleiro, col)
                fazer_jogada(tabuleiro, linha, col, 2)
                if verificar_vitoria(tabuleiro, 2):
                    imprimir_tabuleiro(tabuleiro)
                    print("Jogador 2 venceu!")
                    fim = True
        turno += 1
        turno %= 2

        if not movimentos_validos(tabuleiro):
            print("Empate!")
            fim = True

if __name__ == "__main__":
    main()
