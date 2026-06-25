#Problema - Gostos totais com pagamento de salarios
# Dado uma lista de salarios, calcule o total pago a todos os funcionarios
'''
# Metodo 5Q's para montar um algoritmo

Analise criticamente o problema e descubra:
(tente explicar este ploblema para voce mesmo em voz altra e peca mais infomacoes/investigue mais ate voce compreenda completamente o problema)

1. Quais sao os dados necessarios?
- Uma lista de salarios dos funcionarios

2. O que devo fazer com estes dados?
- Adicionar o salario do usuario a lista de salarios
- Calcular o total pago a todos os funcionarios, somando os salarios da lista
- Exibir o total pago a todos os funcionarios para o usuario

3. Quais as restricoes deste problema?
- A lista de salarios deve conter apenas numeros (salarios)
- Precisamos de pelo menos 2 salarios na lista para fazer a soma

4. Qual e o resultado esperado?
- Exibir o total pago a todos os funcionarios, que é a soma de todos os salarios da lista

5. Qual a sequencia de passos a ser feita para chegar ao resultado esperado?(Pseudocodigo)
- Receber uma lista de salarios
- Somar cada valor da lista ate obter o total
- Exibir o total pago a todos os funcionarios para o usuario

'''
salarios = [1900, 2500, 3000, 3500, 4000]
total = 0
for salario in salarios: # para cada salario na lista de salarios
    total = total + salario # adicione o salario ao total 1900 -. 1900 + 2500 -> 4400 + 3000 -> 7400 + 3500 -> 10900 + 4000 -> 14900

print(total) # exiba o total pago a todos os funcionarios para o usuario