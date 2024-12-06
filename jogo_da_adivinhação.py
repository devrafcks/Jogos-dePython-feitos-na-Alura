def jogar():
    import random


    print("***********")
    print("bem vindo ao jogo de adivinhação!")
    print("***********")

    numero_secreto = random.randrange(1, 21)
    total_de_tentativas = 0
    pontos = 300
    #print(numero_secreto)

    print("Qual o nível de dificuldade?")
    print("[1] Fácil [2] Médio [3] Difícil")
    nivel = int(input("Defina um nível: "))

    if(nivel == 1):
        total_de_tentativas = 7
    elif(nivel == 2):
        total_de_tentativas = 5
    else:
        total_de_tentativas = 3



    for rodadas in range (1, total_de_tentativas + 1):
        print("tentativas {} de {}".format(rodadas, total_de_tentativas))

        chute_str = input("Digite o seu número: ")
        chute = int(chute_str)

        if(chute < 1 or chute> 21):
            print("você deve digitar um número entre 1 e 20")
        
if(__name__ == "__main__"):
    jogar()