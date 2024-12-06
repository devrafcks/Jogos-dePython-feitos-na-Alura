import forca
import jogo_da_adivinhação

def escolher_jogo():
    print("***************")
    print("Escolha um jogo")
    print("***************")

    jogo = int(input("Digite (1) para jogo da adivinhação ou (2) para jogo da forca!\n"))
    if(jogo == 1 ):
        print("\n\n*** você escolheu o jogo da adivinhação! ***\n\n")
        jogo_da_adivinhação.jogar()
    elif(jogo == 2):
        print("\n\n*** você escolheu o jogo da forca! ***\n\n")
        forca.jogar()
if(__name__ == "__main__"):
    escolher_jogo()