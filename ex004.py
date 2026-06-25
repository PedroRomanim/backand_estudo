# Ainda em lacos de repeticao e Continuacao do ex003
'''Syntaxe
while condicao:
    #codigo a ser executado
'''

#tentativas = 0
#while tentativas < 3:
#    print('Tente novamente')
#    tentativas = tentativas + 1
#


#Quando queremos que uma acão continue acontecendo, ate que um
#criterio seja satisfeito.
#Exemplo: So pode logar se digitar a senha correta.
'''
senha = ''
while senha != '123456':
    senha = input('Digite a senha: ')

print('Acesso permitido')

'''
# Garantir que algo esteja preenchido
# So deve continuar se o usuario informar um nome

'''

nome = ''
while nome == '':
    nome = input('Digite seu nome: ')

print(f'Bem vindo {nome}')

'''
# Contadores dentro de While
# Ser avisado as 17hrs do por do sol
# Contar de hora em hora ate chegar as 17hrs
# Ao chegar as 17hrs, exibir: "hora de ver o por do sol"

horario = 0
while horario <= 17:
    print(horario)
    horario = horario + 1

print('Hora de ver o por do sol')