import random

lista = ['Pedra', 'Papel', 'Tesoura']

print("Bem vindo ao Jokenpo do Enzo, para começar digite seu nome!")
print(" ")
nomePlayer = input("Digite seu nome: ")

ganhador = False
ganhadorID = " "

print("Bem-Vindo", nomePlayer)
while(ganhador != True):
    selecBot = random.randrange(0, len(lista))
    jogadaBot = lista[selecBot]
    print("Escolha sua jogada:")
    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura")
    opcPlayer = int(input(""))


    if(opcPlayer == 1 and jogadaBot == 'Pedra'):
        print("Empate")
        print()
    elif(opcPlayer == 1 and jogadaBot == 'Papel'):
        print("Perdeu")
        ganhadorID = "Computador"
        ganhador = True
        print()
    elif(opcPlayer == 1 and jogadaBot == 'Tesoura'):
        print("Ganhou")
        ganhadorID = nomePlayer
        ganhador = True
        print()


    if(opcPlayer == 2 and jogadaBot == 'Pedra'):
        print("Ganhou")
        ganhadorID = nomePlayer
        ganhador = True
        print()
    elif(opcPlayer == 2 and jogadaBot == 'Papel'):
        print("Empate")
        print()
    elif(opcPlayer == 2 and jogadaBot == 'Tesoura'):
        print("Perdeu")
        ganhadorID = "Computador"
        ganhador = True
        print()


    if(opcPlayer == 3 and jogadaBot == 'Pedra'):
        print("Perdeu")
        ganhadorID = "Computador"
        ganhador = True
        print()
    elif(opcPlayer == 3 and jogadaBot == 'Papel'):
        print("Ganhou")
        ganhadorID = nomePlayer
        ganhador = True
        print()
    elif(opcPlayer == 3 and jogadaBot == 'Tesoura'):
        print("Empate")
        print()

if(ganhadorID == "Computador"):
    print("O vencedor foi", ganhadorID)
    print("Obrigado por Jogar!")
elif(ganhadorID == nomePlayer):
    print("O vencedor foi", nomePlayer)
    print("Obrigado por Jogar!")
