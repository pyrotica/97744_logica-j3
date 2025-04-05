import os
os.system("cls || clear")

def print_tabuleiro(tabuleiro):
    for i in range(3):
        print(" | ".join(tabuleiro[i]))
        if i < 2:
            print("-" * 5)

def checar_vitoria(tabuleiro, jogador):
    # Verifica as linhas
    for linha in tabuleiro:
        if linha.count(jogador) == 3:
            return True
    # Verifica as colunas
    for col in range(3):
        if tabuleiro[0][col] == tabuleiro[1][col] == tabuleiro[2][col] == jogador:
            return True
    # Verifica as diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True
    return False

def checar_empate(tabuleiro):
    for linha in tabuleiro:
        if " " in linha:
            return False
    return True

def jogar():
    # Inicializa o tabuleiro
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogadores = ["X", "O"]
    turno = 0  # Começa com o jogador "X"
    
    while True:
        print_tabuleiro(tabuleiro)
        print(f"\nVez do jogador {jogadores[turno]}:")
        
        # Solicita a jogada
        linha = int(input("Escolha a linha (0-2): "))
        coluna = int(input("Escolha a coluna (0-2): "))
        
        # Verifica se a posição está disponível
        if tabuleiro[linha][coluna] != " ":
            print("Posição já ocupada, tente novamente.")
            continue
        
        # Realiza a jogada
        tabuleiro[linha][coluna] = jogadores[turno]
        
        # Verifica se alguém venceu
        if checar_vitoria(tabuleiro, jogadores[turno]):
            print_tabuleiro(tabuleiro)
            print(f"\nJogador {jogadores[turno]} venceu!")
            break
        
        # Verifica se houve empate
        if checar_empate(tabuleiro):
            print_tabuleiro(tabuleiro)
            print("\nO jogo terminou em empate!")
            break
        
        # Alterna o turno
        turno = 1 - turno

# Inicia o jogo
jogar()

