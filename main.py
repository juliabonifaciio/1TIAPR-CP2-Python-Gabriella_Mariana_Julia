# 1. Função para exibir o tabuleiro
def exibir_tabuleiro(tabuleiro):
    print()
    for i in range(3):
        print(tabuleiro[i][0], "|", tabuleiro[i][1], "|", tabuleiro[i][2])
        if i < 2:
            print("---------")
    print()

# 2. Função para verificar se houve um vencedor
def verificar_vencedor(tabuleiro, jogador):
    if tabuleiro[0][0] == jogador and tabuleiro[0][1] == jogador and tabuleiro[0][2] == jogador:
        return True
    if tabuleiro[1][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[1][2] == jogador:
        return True
    if tabuleiro[2][0] == jogador and tabuleiro[2][1] == jogador and tabuleiro[2][2] == jogador:
        return True

    if tabuleiro[0][0] == jogador and tabuleiro[1][0] == jogador and tabuleiro[2][0] == jogador:
        return True
    if tabuleiro[0][1] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][1] == jogador:
        return True
    if tabuleiro[0][2] == jogador and tabuleiro[1][2] == jogador and tabuleiro[2][2] == jogador:
        return True

    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        return True

    return False

# 3. Função para verificar se houve um empate
def verificar_empate(tabuleiro):
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == " ":
                return False
    return True

# 4. Função para verificar se uma jogada é válida
def jogada_valida(tabuleiro, linha, coluna):
    if linha >= 0 and linha <= 2 and coluna >= 0 and coluna <= 2:
        if tabuleiro[linha][coluna] == " ":
            return True
    return False

# 5. Loop principal do jogo
def jogar():
    tabuleiro = [[" ", " ", " "] for _ in range(3)]
    jogador_atual = "X"

    print("=== JOGO DA VELHA ===")
    print("\nJogador 1 = X")
    print("Jogador 2 = O")
    print()

    while True:
        exibir_tabuleiro(tabuleiro)
        print("\nVez do jogador:", jogador_atual)

        linha = int(input("\nDigite a linha (0, 1 ou 2): "))
        coluna = int(input("Digite a coluna (0, 1 ou 2): "))

        if jogada_valida(tabuleiro, linha, coluna):
            tabuleiro[linha][coluna] = jogador_atual
        else:
            print("\nJogada inválida, tente de novo!")
            continue

        if verificar_vencedor(tabuleiro, jogador_atual):
            exibir_tabuleiro(tabuleiro)
            print("\nParabéns! Jogador", jogador_atual, "venceu!")
            break

        if verificar_empate(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print("\nEmpate! Ninguém venceu.")
            break

        if jogador_atual == "X":
            jogador_atual = "O"
        else:
            jogador_atual = "X"

jogar()