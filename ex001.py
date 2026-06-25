#variaveis
# Numeros inteiro(Int)
#idade = 15;
# Numeros decimais(float)
#altura = 1.75;
# Texto(string)
#nome = "João";
# Booleano(true/false)(bool)
#estudante = True;




#Exercicio 1: Salario hora do funcionario
'''
Metodo 5Q's para entender o problema:

Analise criticamente o problema e descubra:
(tente explicar este ploblema para voce mesmo em voz altra e peca mais infomacoes/investigue mais ate voce compreenda completamente o problema)

1. Quais sao os dados necessarios?
- Salario Mensal
- Quantidade de horas trabalhadas

2. O que devo fazer com estes dados?
- Calcular o salario por hora

3. Quais as restricoes deste problema?
- Precisa ter um valor do salario mensal 
- Precisa ter um valor da quantidade de horas trabalhadas
(caberia mais restricoes, porem vamos deixar apenas estas para este exemplo)

4. Qual e o resultado esperado?
- Exibir o valor hora da pessoa, com base no calculo de valor hora

5. Qual a sequencia de passos a ser feita para chegar ao resultado esperado?(Pseudocodigo)
- Pedir o valor do salario mensal
- Guardar esse valor em uma variavel
- Pedir o valor da quantidade de horas trabalhadas
- Guardar esse valor em outra variavel
- Calcular o valor hora, dividindo o salario mensal pela quantidade de horas trabalhadas
(valor_hora = salario mensal / quantidade horas trabalhadas)
- Exibir o valor hora para o usuario
'''

salario_mensal = input("Digite o valor do salario mensal: ")
horas_trabalhadas = input("Digite a quantidade de horas trabalhadas: ")
valor_hora = float(salario_mensal)/ int(horas_trabalhadas)
print(f"O valor hora do funcionario e: R${valor_hora:.2f}")