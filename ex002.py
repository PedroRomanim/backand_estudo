#condicionais - if elif else
'''
E ae Pedro bora dar um rolê?
Se eu terminar o trabalho aqui eu consigo.
'''

# Exemplo 1 
trabalho_terminado = True
if trabalho_terminado == True:
    print("Bora!")
else:
    print("Nao posso sair.")


'''Syntax
if condição:
    #codigo a ser executado se a condição for verdadeira
else:
    #codigo a ser executado se a condição for falsa 
'''
'''
Ei, voce consegue me ajudar a mover essas caixas la para fora hoje a tarde?

Se euestiver livre, sim. Mas se nao der pede para meu irmao te ajudar.
'''

'''

estou_livre = True
if estou_livre == True:
    print("Sim, posso te ajudar.")
else:
    print("Nao posso te ajudar, mas meu irmao pode te ajudar.") 

#Como lidar com mais que 2 condicoes?
Eu cheguei atrasado na aula. Ainda posso entrar?

Se for a primeira ou segunda vez que voce chega atrasadoi, pode sim. 
Mas se for a terceira vez, voce sera suspenso.

'''

# Exercicio 1: Verificar se o usuario pode entrar na aula com base no numero de atrasos

atrasos = int(input("Quantas vezes voce chegou atrasado? "))
if atrasos >= 3:
    print("Voce sera suspenso!")
elif atrasos >= 2:
    print("Mais uma falta e voce sera suspenso!")
elif atrasos >= 1:
    print("Mais duas faltas e voce sera suspenso!")
else:
    print("Pode entrar!")




# Problema
# Crie um progama que recebe dois valores e exibe qual e o maior entre eles.
'''
#Metodo 5Q's para entender o problema:

Analise criticamente o problema e descubra:
(tente explicar este ploblema para voce mesmo em voz altra e peca mais infomacoes/investigue mais ate voce compreenda completamente o problema)

1. Quais sao os dados de entrada necessarios?
- Dois numeros que o usuario ira digitar

2. O Que devo fazer com estes dados?
- Comparar os dois numeros e descobrir qual e o maior

3. Quais sao as restricoes deste problema?
- Os numeros precisam ser validos (numeros reais)
- O programa precisa lidar com o caso de os numeros serem iguais

4. Qual e o resultado esperado?
- Que o programa exiba qual e o maior numero, ou se os numeros sao iguais

5. Qual a sequencia de passos a ser feita para chegar ao resultado esperado?(Pseudocodigo)
- Pedir o usuario para digitar o primeiro numero
- Pedir o usuario para digitar o segundo numero
- Comparar os dois numeros e exibir o maior, ou uma mensagem dizendo que os numeros sao iguais

'''

#Exercicio 2: Comparar dois numeros e exibir o maior
primeiro_valor = int(input("Digite o 1º valor: "))
segundo_valor = int(input("Digite o 2º valor: "))
if primeiro_valor > segundo_valor:
    print("O primeiro e o maior valor!")
elif segundo_valor > primeiro_valor:
    print("O segundo e o maior valor!")
else:
    print("Os valores sao iguais, digite valores diferentes para comparar.")
