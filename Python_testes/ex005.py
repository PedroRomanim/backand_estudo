# Cenario real - Gerenciador de login simples
'''
Crie um gerenciador de login simples, com o maximo de 3 tentativas.
(teremos apenas um unico usuario e senha permitido)

Usuario: pedro
Senha: pedro062

Apos 3 tentativas, se o ususario estiver errado exibir:
"Aguarde 30 minutos antes de tentar novamente"

Se o ususrio acertar o usuario e senha, exibir:
"Login feito com sucesso"

--------------------------------------------------

Metodo 5Q's para entender o problema:

nalise criticamente o problema e descubra:
(tente explicar este ploblema para voce mesmo em voz altra e peca mais infomacoes/investigue mais ate voce compreenda completamente o problema)

1.Quais sao os tipos de dados de entrada necessarios?
- O nome de usuario e a senha

2.O que devo fazer com estes dados?
- Valida-los e verificar se correspondem ao usuario e senha corretos

3.Quais sao as restricoes deste problema?
- O usuario tem no maximo 3 tentativas para acertar o login. 
- O usuario deve preencher o nome de usuario e senha

4.Qual e o resultado esperado?
- Login feito com sucesso se o usuario e senha estiverem corretos
- Quaso o usuario errar 3 vezes, exibir a mensagem de aguardar 30 minutos

5.Qual a sequencia de passos a ser feita para chegar ao resultado esperado?(Pseudocodigo)
- Definir o usuario e senha corretos
- Receber o nome de usuario 
- Receber a senha
- Criar um contador de tentativas
- Enquanto o contador de tentativas for menor que 3:
    - Solicitar ao usuario que insira o nome de usuario e senha
    - Verificar se o nome de usuario e senha correspondem aos valores corretos
    - Se corresponderem, exibir "Login feito com sucesso" e encerrar o programa
    - Se não corresponderem, incrementar o contador de tentativas e exibir uma mensagem de erro
- Se o contador de tentativas atingir 3, exibir "Aguarde 30 minutos antes de tentar novamente"
- Fim do programa

'''

usuario = ''
senha = ''
tentativas = 0

while (usuario != 'Pedro' or senha != 'pedro062') and tentativas < 3:
    usuario = input('Digite o nome de usuario: ')
    senha = input('Digite a senha: ')
    tentativas += 1

if usuario == 'Pedro' and senha == 'pedro062':
    print('Login feito com sucesso')
else:
    print('Aguarde 30 minutos antes de tentar novamente')