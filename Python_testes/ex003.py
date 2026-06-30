# Lacos de repeticao
#For nunca inclui o ultimo numero, entao se eu quiser incluir o 10, preciso colocar 11

#for iten in range(2, 11, 2):
#    print(iten)

#Listas

'''
nomes = ['Maria', 'Joao', 'Pedro', 'Ana']
for nome in nomes:
    print(nome)

#As listas podem ter mais de um tipo de dado
lista = [4, "Pedro", 3.14, False]
for item in lista:
    print(item)

'''
#Listas e condicionais
#idades = [15, 22, 30, 17, 45]
#for idade in idades:
#    if idade >= 18:
#        print(f'{idade} e maior de idade')
#    else:
#        print(f'{idade} nao e maior de idade')
#Exibir quem e maior de idade e quem nao e, usando a lista de idades

'''
Exemplo pratico: Validade de senhas

Problema:
Voce trabalha em um sistema que precisa verificar se todas as senhas digitadas
por usuarios sao validas

Para ser considerada valida, a senha deve ter pelo menos 6 caracteres.
---

Metodo 5Q's para entender o problema:

nalise criticamente o problema e descubra:
(tente explicar este ploblema para voce mesmo em voz altra e peca mais infomacoes/investigue mais ate voce compreenda completamente o problema)

1.Quais sao os tipos de dados de entrada necessarios?
- A senha digitada pelo usuario (string)

2.O que devo fazer com estes dados?
- Verificar se a senha tem 6 ou mais caracteres e exibir uma mensagem de validacao

3.Quais sao as restricoes deste problema?
- A senha deve ser uma string
- A senha deve ter pelo menos 6 caracteres
- O programa deve lidar com o caso de a senha ser vazia ou conter apenas espacos

4.Qual e o resultado esperado?
- Que o programa exiba uma mensagem indicando se a senha e valida ou invalida

5.Qual a sequencia de passos a ser feita para chegar ao resultado esperado?(Pseudocodigo)
- Pedir o usuario para digitar a senha
- Verificar o comprimento da senha 
- Se ela tiver 6 ou mais caracteres, exibir "Senha valida!"
- Caso contrario, exibir "Senha invalida!"

'''
# len(variavel) e uma funcao que retorna o comprimento de uma string ou lista
#len(senha) >= 6 ou nao 

#senhas = ["abc", "123456", "senha123", "python123", "pedro"]
#for senha in senhas:
#        if len(senha) >= 6:
#             print('Acesso permitido!')
#        else: 
#            print('Acesso negado!')
        
        
