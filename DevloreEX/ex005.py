import random


sorteio = random.randint(0, 50)
sorteio = 25
usuario_valor = 0

def tente_de_novo():
    input("Precione Enter para tentar de novo!")

usuario_valor = input(float("Chute um numero: "))
while usuario_valor != sorteio:
    if usuario_valor <= sorteio:
        print("chutou baixo! tente de novo!")
        tente_de_novo()
    elif usuario_valor >= sorteio:
        print("Chutou alto! tente de nov!")
        tente_de_novo()
    elif usuario_valor == sorteio:
        print("Parabens voce acertou!")
        tente_de_novo()