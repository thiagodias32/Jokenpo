def obter_escolha(jogador):
    while True:
            escolha = int(input(f"{jogador}, escolha:\n"
                                "1 para pedra\n"
                                "2 para papel\n"
                                "3 para tesoura\n"
                                "Digite sua escolha: "))
            if escolha in [1, 2, 3]:
                return escolha

def determinar_vencedor(escolha1, escolha2):
    if escolha1 == escolha2:
        return 0
    elif (escolha1 == 1 and escolha2 == 3) or (escolha1 == 2 and escolha2 == 1) or (escolha1 == 3 and escolha2 == 2):
        return 1
    else:
        return 2

def menu():
    pontosJ1 = 0
    pontosJ2 = 0

    nome1 = input("Jogador 1, digite seu nome: ")
    nome2 = input("Jogador 2, digite seu nome: ")

    for i in range(3):
        escolha1 = obter_escolha(nome1)
        escolha2 = obter_escolha(nome2)

        vencedor = determinar_vencedor(escolha1, escolha2)

        if vencedor == 0:
            print("Foi empate, ninguém fez pontos.")
        elif vencedor == 1:
            print(f"{nome1} fez 1 ponto nesta rodada.")
            pontosJ1 += 1
        else:
            print(f"{nome2} fez 1 ponto nesta rodada.")
            pontosJ2 += 1

        print("")

    if pontosJ1 > pontosJ2:
        print(f"{nome1} ganhou! Parabéns!!!!!")
    elif pontosJ2 > pontosJ1:
        print(f"{nome2} ganhou! Parabéns!!!!!")
    else:
        print("Empate, ninguém ganhou.")
