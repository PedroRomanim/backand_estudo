# Progeto 1 - Fatorial de um numero
# Crie um programa que receba um numero e imprima o seu fatorial. 
# Oque é fatorial? O fatorial de um numero n é o produto de todos os numeros inteiros positivos menores ou iguais a n.
# Exemplo: O fatorial de 5 é 5 * 4 * 3

'''
# Metodo 5Q's para montar um algoritmo

Analise criticamente o problema e descubra:
(tente explicar este ploblema para voce mesmo em voz altra e peca mais infomacoes/investigue mais ate voce compreenda completamente o problema)

1. Quais sao os dados necessarios?
- Um numero inteiro positivo que o usuario ira digitar para calcular o fatorial

2. O que devo fazer com estes dados?
- Calcular o fatorial do numero fornecido pelo usuario

3. Quais as restricoes deste problema?
- O numero fornecido deve ser um inteiro positivo

4. Qual e o resultado esperado?
- Exibir o fatorial do numero fornecido para o usuario

5. Qual a sequencia de passos a ser feita para chegar ao resultado esperado?(Pseudocodigo)
- Receber um numero inteiro positivo do usuario
- Calcular o fatorial do numero
- Exibir o resultado para o usuario

'''
# Programa para calcular o fatorial de um numero
print("Calculadora de Fatorial")
print("-----------------------")
numero = int(input("Digite um numero: "))
fatorial = 1
if numero > 0 and type(numero) == int:
    for iten in range(1, numero + 1):
        fatorial = fatorial * iten
    print(f'O fatorial de {numero} é {fatorial}')
else:
    print("Digite um numero inteiro positivo!")


'''
# Codigo do professor para calcular o fatorial de um numero

numero = int(input("Digite o numero para calcular o fatorial: "))
if numero > 0 and type(numero) == int:
    fatorial = 1
    for iten in range(1, numero + 1):
        print(f'{fatorial} * {iten}')
        fatorial = fatorial * iten
        print(f'{fatorial}')
    print(f'O fatorial de {numero} é {fatorial}') 
else:
    print("Digite um numero inteiro positivo!")

'''