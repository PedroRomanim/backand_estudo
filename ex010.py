# Projeto 3 - Medidor de velocidade
'''
Crie um programa que receba do usuario um valor que represente a velocidade em uma via 
cuja velocidade maxima permitida e de 80 km/h.

Com base nesse valor, o programa deve informar se o motorista levou uma muta leve, grave ou gravissima.

Se a velocidade estiver abaixo ou igual a 80 km/h exiba: "nao ouve multa".
Se estiver ate 10 km/h acima, exiba: "levou uma multa leve".
Se estiver entre 11 km/h e 20 km/h acima, exiba: "levou uma multa grave"
Se estiver 20 km/h acima, exiba: "Levou uma multa gravissima".

'''
# Metodo 5Q's para montar um algoritmo

'''

Analise criticamente o problema e descubra:
(tente explicar este ploblema para voce mesmo em voz altra e peca mais infomacoes/investigue mais ate voce compreenda completamente o problema)

1. Quais sao os dados necessarios?
- Pedir a velocidade ao usuario

2. O que devo fazer com estes dados?
- Comparar-la e ver em qual das multas se encaixa

3. Quais as restricoes deste problema?
- O usuario precisa dizer a velocidade

4. Qual e o resultado esperado?
- Que exiba as infomacoes de acordo com que elas se encaixa

5. Qual a sequencia de passos a ser feita para chegar ao resultado esperado?(Pseudocodigo)
- Pedir para o usuario digitar a velocidade
- vem em qual se encaixa
    - Se estiver abaixo ou igual a 80 km/h exibir ("nao ouve multa".)
    - Se estiver ate 10 km/h acima, exiba: "levou uma multa leve".
    - Se estiver entre 11 km/h e 20 km/h acima, exiba: "levou uma multa grave".
    - Se estiver 20 km/h acima, exiba: "Levou uma multa gravissima".

'''

velocidade_usuario = int(input("Digite sua velocidade: "))
exesso = velocidade_usuario - 80

if exesso <= 0:
    print("Nao ouve multa")
elif exesso <= 10:
    print("Levou uma multa leve")
elif exesso < 20:
    print("Levou uma multa grave")
else:
    print("Levou uma multa gravissima")
