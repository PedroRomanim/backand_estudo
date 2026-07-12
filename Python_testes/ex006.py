#listas
'''
precos = [10, 20, 30, 40, 50]
# Da para acessar os elementos da lista usando índices
# o indice nada mais é a posição do elemento na lista, começando do 0
Ex:
precos = [10, 20, 30, 40, 50]
[0] # retorna o primeiro elemento da lista, que é 10
[1] # retorna o segundo elemento da lista, que é 20
[2] # retorna o terceiro elemento da lista, que é 30
[3] # retorna o quarto elemento da lista, que é 40
[4]  # retorna o quinto elemento da lista, que é 50
precos = [10, 20, 30, 40, 50]
print(precos[0]) # imprime o primeiro elemento da lista, que é 10
print(precos[1]) # imprime o segundo elemento da lista, que é 20
etc...

Os valores para acerssar os indices sempre vao ser numericos
por mais que a lista tenha elementos de outros tipos, os indices sempre serão numericos

'''
#precos = [10, 20, 30, 40, 50]
#print(precos[1]) # imprime o primeiro elemento da lista, que é 10

'''
# Encontrar o índice de um elemento na lista   
nomes = ['Brasil', 'Argentina', 'Uruguai', 'Paraguai', 'EUA']
print(nomes.index('Uruguai')) # retorna o índice do elemento 'Uruguai', que é 2
print(nomes.index('EUA')) # retorna o índice do elemento 'EUA', que é 4 
e assim por diante

Outro ponto a se atentar e que as listas em python podem conter elementos de tipos diferentes, ou seja, uma lista pode conter números, strings, booleanos, etc.
Ex:
lista_mista = [10, 'Brasil', True, 3.14]

'''

# Manipular - add novos itens a lista
salarios = [1900, 2500, 3000]
salario_usuario = float(input('Digite o seu salário: '))
salarios.append(salario_usuario) # adiciona o salário do usuário à lista de salários
print(salarios) # imprime a lista de salários atualizada
