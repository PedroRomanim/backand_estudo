import pyfiglet

def menu():
    logo = pyfiglet.figlet_format("\nCofrinho Digital!", font='Slant')
    print(logo)
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
    input("\nPressione Enter para retonar ao menu!")  



saldo_usuario = 0
opcoes_menu = ""

while opcoes_menu != "4":
    opcoes_menu = menu()
    if opcoes_menu == "1":
        depositar = float(input("Qual o valor desejado: "))
        if depositar > 0:
          saldo_usuario += depositar
          print(f"Deposito feito com sucesso! No valor de: {depositar:.2f} R$")   
          retorno_menu()   
        else:
            mensagem("Erro ao efetuar o deposito")
            retorno_menu()
    elif opcoes_menu == "2":
        saque = float(input("Qual valor que deseja sacar: "))
        
        if saque > saldo_usuario:
            mensagem("Saldo insuficiente!")
            retorno_menu()
        else:
            saldo_usuario -= saque
            mensagem("Saque realizado com sucesso!")
            retorno_menu()
    elif opcoes_menu == "3":
        linha()
        print(f"Seu saldo e de R${saldo_usuario:.2f}!")
        linha()
        retorno_menu()    
    elif opcoes_menu == "4":
        break
    
    else:
        mensagem("Opção invalida!")
        retorno_menu()