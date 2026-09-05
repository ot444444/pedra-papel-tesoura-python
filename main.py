import random

# Escolha da categoria de Jogo:
# Humano com Humano, Humano com Computador ou Computador com Computador

print("Escolha a Categoria: ")
categoria = int(input("1 para HxH ; 2 para HxC ; 3 para CxC : "))

while categoria < 1 or categoria > 3:
    print("Categoria Invalida")
    categoria = int(input("1 para HxH ; 2 para HxC ; 3 para CxC : "))

# Valores para opcoes de jogo
pedra = 1
tesoura = 2
papel = 3

ponto1 = 0
ponto2 = 0

escolha1 = 0
escolha2 = 0

loop = True

while loop:

    # Jogo Humano x Humano
    if categoria == 1:

        print("Pedra = 1, Tesoura = 2, Papel = 3")

        escolha1 = int(input("Digite sua escolha: "))

        while escolha1 < 1 or escolha1 > 3:
            print("Escolha Invalida")
            escolha1 = int(input("Digite sua escolha: "))

        if escolha1 == 1:
            print("O Jogador um Escolheu Pedra")
        elif escolha1 == 2:
            print("O Jogador um Escolheu Tesoura")
        else:
            print("O Jogador um Escolheu Papel")

        escolha2 = int(input("Digite sua escolha: "))

        while escolha2 < 1 or escolha2 > 3:
            print("Escolha Invalida")
            escolha2 = int(input("Digite sua escolha: "))

        if escolha2 == 1:
            print("O Jogador dois Escolheu Pedra")
        elif escolha2 == 2:
            print("O Jogador dois Escolheu Tesoura")
        else:
            print("O Jogador dois Escolheu Papel")

    # Jogo Humano x Maquina
    elif categoria == 2:

        print("Pedra = 1, Tesoura = 2, Papel = 3")

        escolha1 = int(input("Digite sua escolha: "))

        while escolha1 < 1 or escolha1 > 3:
            print("Escolha Invalida")
            escolha1 = int(input("Digite sua escolha: "))

        if escolha1 == 1:
            print("O Jogador um Escolheu Pedra")
        elif escolha1 == 2:
            print("O Jogador um Escolheu Tesoura")
        else:
            print("O Jogador um Escolheu Papel")

        escolha2 = random.randint(1, 3)

        if escolha2 == 1:
            print("A Maquina Escolheu Pedra")
        elif escolha2 == 2:
            print("A Maquina Escolheu Tesoura")
        else:
            print("A Maquina Escolheu Papel")

    # Jogo Maquina x Maquina
    elif categoria == 3:

        escolha1 = random.randint(1, 3)
        escolha2 = random.randint(1, 3)

        if escolha1 == 1:
            print("A Maquina um Escolheu Pedra")
        elif escolha1 == 2:
            print("A Maquina um Escolheu Tesoura")
        else:
            print("A Maquina um Escolheu Papel")

        if escolha2 == 1:
            print("A Maquina dois Escolheu Pedra")
        elif escolha2 == 2:
            print("A Maquina dois Escolheu Tesoura")
        else:
            print("A Maquina dois Escolheu Papel")

    # Regras Pedra, Papel e Tesoura
    if escolha1 == 1 and escolha2 == 2:
        print("Vitoria do Primeiro Jogador")
        ponto1 += 1

    elif escolha1 == 1 and escolha2 == 3:
        print("Vitoria do Segundo Jogador")
        ponto2 += 1

    elif escolha1 == 2 and escolha2 == 1:
        print("Vitoria do Segundo Jogador")
        ponto2 += 1

    elif escolha1 == 2 and escolha2 == 3:
        print("Vitoria do Primeiro Jogador")
        ponto1 += 1

    elif escolha1 == 3 and escolha2 == 1:
        print("Vitoria do Primeiro Jogador")
        ponto1 += 1

    elif escolha1 == 3 and escolha2 == 2:
        print("Vitoria do Segundo Jogador")
        ponto2 += 1

    else:
        print("Empate")

    print(f"{ponto1} x {ponto2}")

    print("Voce quer continuar jogando")
    continuar = int(input("1 para Sim e 2 para Nao: "))

    while continuar < 1 or continuar > 2:
        print("Valor invalido")
        continuar = int(input("1 para Sim e 2 para Nao: "))

    if continuar == 2:
        print(f"Placar final: {ponto1} x {ponto2}")
        loop = False

print("Fim de jogo. Obrigado por jogar; Jogo por: Otavio K e Gabriel G.")
