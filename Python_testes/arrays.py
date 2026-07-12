# ============================================================================
# EXEMPLOS DE ARRAYS E MATRIZES EM PYTHON
# ============================================================================

# ============================================================================
# 1. ARRAY UNIDIMENSIONAL (Lista com uma dimensão)
# ============================================================================

print("=" * 70)
print("1. EXEMPLO DE ARRAY UNIDIMENSIONAL")
print("=" * 70)

# Criando um array unidimensional (lista em Python)
numeros = [10, 20, 30, 40, 50]

print(f"\nArray unidimensional: {numeros}")
print(f"Tipo: {type(numeros)}")
print(f"Comprimento (quantidade de elementos): {len(numeros)}")

# Acessando elementos individuais pelo índice (começando do 0)
print("\n--- Acessando elementos pelo índice ---")
print(f"Elemento no índice 0: {numeros[0]}")
print(f"Elemento no índice 2: {numeros[2]}")
print(f"Elemento no índice 4: {numeros[4]}")
print(f"Último elemento (índice -1): {numeros[-1]}")

# Iterando sobre os elementos
print("\n--- Iterando sobre o array ---")
print("Valores: ", end="")
for numero in numeros:
    print(numero, end=" ")
print()

# Iterando com índice
print("\nValores com índices:")
for indice, valor in enumerate(numeros):
    print(f"  Índice {indice}: {valor}")

# Operações com arrays unidimensionais
print("\n--- Operações com o array ---")
numeros.append(60)  # Adiciona um elemento no final
print(f"Após adicionar 60: {numeros}")

numeros.insert(0, 5)  # Insere um elemento no índice 0
print(f"Após inserir 5 no início: {numeros}")

numeros.remove(20)  # Remove o elemento de valor 20
print(f"Após remover 20: {numeros}")

print(f"Soma de todos os elementos: {sum(numeros)}")
print(f"Maior elemento: {max(numeros)}")
print(f"Menor elemento: {min(numeros)}")


# ============================================================================
# 2. MATRIZ MULTIDIMENSIONAL (Lista com múltiplas dimensões - Matriz 2D)
# ============================================================================

print("\n" + "=" * 70)
print("2. EXEMPLO DE MATRIZ MULTIDIMENSIONAL (2D)")
print("=" * 70)

# Criando uma matriz 3x3 (3 linhas e 3 colunas)
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("\nMatriz 3x3:")
print("Tipo: Lista de listas (estrutura multidimensional)")

# Exibindo a matriz de forma formatada
print("\n--- Exibição da matriz ---")
for linha in matriz:
    print(linha)

# Acessando elementos específicos [linha][coluna]
print("\n--- Acessando elementos específicos [linha][coluna] ---")
print(f"Elemento na linha 0, coluna 0: {matriz[0][0]}")
print(f"Elemento na linha 1, coluna 1: {matriz[1][1]}")
print(f"Elemento na linha 2, coluna 2: {matriz[2][2]}")

# Acessando uma linha inteira
print("\n--- Acessando uma linha inteira ---")
print(f"Primeira linha (índice 0): {matriz[0]}")
print(f"Segunda linha (índice 1): {matriz[1]}")
print(f"Terceira linha (índice 2): {matriz[2]}")

# Iterando sobre a matriz com índices
print("\n--- Iterando sobre a matriz com índices ---")
for i in range(len(matriz)):  # i percorre as linhas
    for j in range(len(matriz[i])):  # j percorre as colunas
        print(f"matriz[{i}][{j}] = {matriz[i][j]}", end="  ")
    print()  # Nova linha após cada linha da matriz

# Iterando sobre a matriz diretamente
print("\n--- Iterando sobre a matriz (sem índices) ---")
for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print()

# Operações com a matriz
print("\n--- Operações com a matriz ---")
matriz[0][0] = 10  # Modifica um elemento
print(f"Após modificar matriz[0][0] para 10:")
for linha in matriz:
    print(linha)

# Soma de todos os elementos
soma_total = sum(sum(linha) for linha in matriz)
print(f"\nSoma de todos os elementos: {soma_total}")

# Contando linhas e colunas
linhas = len(matriz)
colunas = len(matriz[0])
print(f"Dimensões da matriz: {linhas} linhas × {colunas} colunas")

print("\n" + "=" * 70)
