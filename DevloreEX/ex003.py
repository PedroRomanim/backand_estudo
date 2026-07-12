Soma_total = 0
alunos= {}
quantidade_alunos = 0

print("=============================================")
quantidade_alunos = int(input(f"Quantos alunos deseja cadastrar?\n"))

print("=============================================")
for i in range(quantidade_alunos):
    nome = str(input(f"Nome {i + 1}: "))
    nota = float(input(f"Qual a nota {i + 1}: "))
    alunos[nome] = nota
    Soma_total += nota   

Resultado = Soma_total / len(alunos)

#Para obter a maior nota
maior_nota = max(alunos, key = alunos.get)
#Para obter a menor note
menor_nota = min(alunos, key = alunos.get)

print("=============================================")
for nome, nota in alunos.items():
    print(nome, "->", nota)
print("=============================================")
print("Media da turma: ", Resultado)
print("==============================================================================")
print(f"O aluno com a maior nota foi: {maior_nota}, Com a nota: {alunos[maior_nota]}")
print("==============================================================================")
print(f"O aluno com a menor nota foi: {menor_nota}, Com a nota: {alunos[menor_nota]}")