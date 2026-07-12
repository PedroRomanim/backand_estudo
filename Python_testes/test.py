#nome = input("Qual é o seu nome? ")
#senha = input("Digite a sua senha: ")
#usuario = "admin"
#senha_acesso = "admin123"

#if nome == usuario and senha == senha_acesso:
#    print("Acesso concedido! Bem-vindo, " + nome + "!")
#elif nome == usuario and senha != senha_acesso:
#    print("Senha incorreta. Tente novamente.")
#elif nome != usuario and senha == senha_acesso:
#    print("Usuário incorreto. Tente novamente.")
#else:
#    print("Usuário e senha incorretos. Tente novamente.")


#banco de dados de usuarios
usuarios = {
    "admin": "admin123",
    "user1": "senha1",
    "user2": "senha2"
}

while True:
    nome = input("Qual é o seu nome? ")
    senha = input("Digite a sua senha: ")

    if nome in usuarios and senha == usuarios[nome]:
        print("Acesso concedido! Bem-vindo, " + nome + "!")
        break
    elif nome in usuarios and senha != usuarios[nome]:
        print("Senha incorreta. Tente novamente.")
    elif nome not in usuarios:
        print("Usuário incorreto. Tente novamente.")


#Uma leve explicacao do codigo acima e oque eu entendi, e o que eu achei interessante.
'''
O codigo acima foi gerado pela propria IA do VS Code, porem apesar de nao enteder
por completo eu consegui entender a logica do codigo. 
Achei interessante pois ponhado a mao na massa e vendo o codigo funcionando, consegui entender melhor a logica de repeticao e condicional.
usuarios e um dicionario que armazena os usuarios e suas respectivas senhas,
o while True: cria um loop infinito que so sera interrompido quando o usuario digitar as credenciais corretas. ou seja True.
Ainda nao entendi o break, mas sei que ele serve para sair do loop, pois acho que vem de quebrar (break) no caso o loop.
---
O primeiro codigo nas linhas 1 a 13, foi oque eu escrevi, so com oque sabia e aprendi ate agora.
Ele tem uma logica mais simples, onde ele verifica se o nome e a senha digitados sao iguais ao usuario e senha predefinidos,
e entao concede ou nega o acesso.

'''