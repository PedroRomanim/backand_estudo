import queue # Importando a biblioteca de filas (queue) em Python

#Criando uma FIla (FIFO) em Python
fila = queue.Queue()

# Adicionando elementos à fila
fila.put("Primeiro")
fila.put("Segundo")
fila.put("Terceiro")
#print("Fila atual:", list(fila.queue))

# Removendo elementos da fila
print("Removendo elementos da fila:")
while not fila.empty():
    print(fila.get())
print("Fila vazia:", fila.empty())
## Explicação:
'''
- FIFO (First In, First Out) é uma estrutura de dados onde o primeiro elemento inserido é o primeiro a ser removido.
- Em uma fila, os elementos são adicionados no final e removidos do início.    
- No exemplo acima, usamos a biblioteca `queue` do Python para criar uma fila.
- O método `put()` é usado para adicionar elementos à fila, enquanto o método `get()` é usado para remover elementos da fila.
- O loop `while` continua removendo elementos da fila até que ela esteja vazia, e o método `empty()` é usado para verificar se a fila está vazia.  

'''