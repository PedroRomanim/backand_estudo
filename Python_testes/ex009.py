# Projeto 2 - Chute um numero
'''
Escreva um progamaque, ao iniciar, gere um valor aleatorio de 1 a 10 e permita que o
usuario chute um numero ate acertar o valor gerado.

O programa deve informar se o chute foi maior, menor ou igualk ao valor aleatorio gerado no inicio.

'''

# Metodo 5Q's para montar um algoritmo

'''

Analise criticamente o problema e descubra:
(tente explicar este ploblema para voce mesmo em voz altra e peca mais infomacoes/investigue mais ate voce compreenda completamente o problema)

1. Quais sao os dados necessarios?
- Um valor aleatrio que o progama gere de 1 a 10
- Um valor de 1 a 10 que usuario vai digitar

2. O que devo fazer com estes dados?
- Compara se valor que o usuario digitou e igual, baixo ou alto em comparacao ao valor gerado aleatoriamente 

3. Quais as restricoes deste problema?
- So pode ser numeros inteiros de 1 a 10 

4. Qual e o resultado esperado?
- Que o progama informe se o chute foi alto, baixo ou igual ae valor aleatorio

5. Qual a sequencia de passos a ser feita para chegar ao resultado esperado?(Pseudocodigo)
- Gerar um valor aleatorio de 1 a 10
- Receber um valor de 1 a 10 do usuario
- Comparar esses dois 
    - Se o chute for alto exibir "Chutou alto!"
    - Se o chte for baixo exibir "Chutou baixo!"
    - Repetir os passos acima ate o usuario acerta 
    - Caso o chute seja igual exibir "Na mosca!"
- Finalizar o progama.

'''

import random
valor_aleatorio = random.randint(1, 10)

while (valor_aleatorio != valor_usuario):
  valor_usuario = int(input("Digite um valor: "))
  if valor_usuario > valor_aleatorio:
        print("Chutou alto!")
  elif valor_usuario < valor_aleatorio:
         print("Chutou baixo!")
  else:
        print("Na mosca!")
        break