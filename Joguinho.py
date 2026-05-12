import random

tentativas = int(0)
valor = int(0)
jogoOn = True

chute = random.randint(1, 100)

while jogoOn == True:
    print(f"Tentativas restantes: {tentativas}/5")
    valor = int(input("Digite um valor inteiro de 1 a 100: "))
    
    if valor == chute:
        print("Parabéns você acertou!")
        jogoOn = False

    elif tentativas >= 4:
        print("Você Fracassou!")
        print(f"O valor era: {chute}")
        jogoOn = False

    elif valor < chute:
        print("O valor é maior, tente novamente!")
        tentativas += 1

    elif valor > chute:
        print("O valor é menor, tente novamente!")
        tentativas += 1
