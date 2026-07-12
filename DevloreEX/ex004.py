#Imports
#import pyfiglet


#Funcoes
def menu():
    print("|---MENU---")
    print("|---[1]-Depositar---")
    print("|---[2]-Sacar---")
    print("|---[3]-Verificar Saldo---")
    print("|---[4]-Sair---")
    return input(f"Escolha: ")

def linha():
    print("|---------------------------------------|")

def mensagem(texto):
    linha()
    print(texto)
    linha()

def retorno_menu():
    input("\nPressione Enter para retornar ao menu!")  


def depositar():
    global saldo_usuario
    valor = float(input("Qual o valor desejado: "))
    if valor > 0:
        saldo_usuario += valor
        print(f"Deposito feito com sucesso! No valor de: {valor:.2f} R$")   
        retorno_menu()
    else:
        mensagem("Erro ao efetuar o deposito")
        retorno_menu()

def saque():
        global saldo_usuario
        valor_saque = float(input("Qual valor que deseja sacar: "))
        if valor_saque <= 0:
            mensagem("O valor do saque deve ser maior que zero!")
            retorno_menu()
        elif valor_saque > saldo_usuario:
            mensagem("Saldo insuficiente!")
            retorno_menu()
        else:
            saldo_usuario -= valor_saque
            mensagem("Saque realizado com sucesso!")
            retorno_menu()

def mostrar_saldo():
    linha()
    print(f"Seu saldo é de R${saldo_usuario:.2f}!")
    linha()
    retorno_menu()  


#Variaveis
saldo_usuario = 0
opcoes_menu = ""

#logo = pyfiglet.figlet_format("\nCofrinho Digital!", font='Slant')

while opcoes_menu != "4":
    opcoes_menu = menu()
    if opcoes_menu == "1":
       depositar()
    elif opcoes_menu == "2":
        saque()
    elif opcoes_menu == "3":
        mostrar_saldo()
    elif opcoes_menu == "4":
        break
    
    else:
        mensagem("Opção invalida!")
        retorno_menu()