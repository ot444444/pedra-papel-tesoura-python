import random  ##import random

print ("Escolha a Categoria : ") ## escolha da categoria
categoria = int(input("1 para HxH ; 2 para HxC ; 3 para CxC : ")) ## input da escolha

while categoria < 1 or categoria > 3: ## loop escolhas invalidas
    print("Categoria Invalida") ## aviso
    categoria = int(input("1 para HxH ; 2 para HxC ; 3 para CxC : ")) ## repetir

## variaveis
pedra = 1
tesoura = 2
papel = 3
ponto1 = 0
ponto2 = 0
escolha1 = 0
escolha2 = 0

## funacao do jogo
def jogo(escolha1, escolha2): ## criando func
    global ponto1
    global ponto2
    if escolha1 == escolha2:
        print("Empate!!")
    elif escolha1 == 1:  # J1 escolheu pedra
        if escolha2 == 2:
            print("J1 Ganhou!!")
            ponto1 += 1
        elif escolha2 == 3:
            print("J2 Ganhou!!")
            ponto2 += 1
    elif escolha1 == 2:  # J1 escolheu tesoura
        if escolha2 == 1:
            print("J2 Ganhou!!")
            ponto2 += 1
        elif escolha2 == 3:
            print("J1 Ganhou!!")
            ponto1 += 1
    elif escolha1 == 3:  # J1 escolheu papel
        if escolha2 == 1:
            print("J1 Ganhou!!")
            ponto1 += 1
        elif escolha2 == 2:
            print("J2 Ganhou!!")
            ponto2 += 1
    print(f"Placar: {ponto1} X {ponto2}")

## funcao para mostrar as ecolhas
def mostrar_escolha(jogador, escolha): ## criando func
    if escolha == 1: ## escolhe pedra
        print(f"O {jogador} escolheu pedra") ## avisa
    elif escolha == 2: ## escolhe tesoura
        print(f"O {jogador} escolheu tesoura") ## avisa
    elif escolha == 3: ## escolhe papel
        print(f"O {jogador} escolheu papel") ## avisa

## funcao para verificacao e pedir escolha
def pedir_escolha(jogador): ## criando func
    print("Pedra = 1, Tesoura = 2, Papel = 3") ## escolhas
    print(f"Escolha do {jogador}") ## aviso
    escolha = int(input("Digite sua escolha: ")) ## pede escolha

    while escolha < 1 or escolha > 3: ## loop verificacao de escolha
        print("Escolha invalida") ## aviso
        print("Pedra = 1, Tesoura = 2, Papel = 3") ## tabela
        escolha = int(input("Digite sua escolha : ")) ## pede escolha novamente

    return escolha ## retorna escolha para a memoria

loop = True ## ativa loop

while loop: ## enquanto loop
    ## escolhas
    if categoria == 1: ## categoria 1
        escolha1 = pedir_escolha("J1") ## pedindo escolha J1
        mostrar_escolha("J1", escolha1) ## mostra escolha J1
        escolha2 = pedir_escolha("J2") ## pedindo escolha J1
    elif categoria == 2: ## categoria 2
        escolha1 = pedir_escolha("J1") ## pedindo escolha J1
        mostrar_escolha("J1", escolha1) ## mostra escolha J1
        escolha2 = random.randint(1, 3) ## escolha random J2
    else: ## categoria 3
        escolha1 = random.randint(1, 3) ## escolha random J1
        mostrar_escolha("J1", escolha1) ## mostra escolha J1
        escolha2 = random.randint(1, 3) ## escolha random J2
    mostrar_escolha("J2", escolha2) ## mostra escolha J2

    jogo(escolha1, escolha2) ## ativa jogo
    print("Voce quer continuar jogando") ## quer continuar?
    continuar = int(input("1 para Sim e 2 para Nao : ")) ## resposta

    while continuar < 1 or continuar > 2: ## verificacao
        print("Valor invalido") ## aviso
        continuar = int(input("1 para Sim e 2 para Nao : ")) ## nova resposta
    if continuar == 2: ## se nao quiser continuar
        print(f"placar final: {ponto1} x {ponto2}") ## placar final
        loop = False ## encerra loop

print("Fim de jogo. Obrigado por jogar ; Jogo por: Otavio K e Gabriel G.") ## msg do fim




    
               
            
