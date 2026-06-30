'''
Estrutura de Dados - LIFO (Last In, First Out)
Ou PILHA (Stack)

Como funciona:
- O último elemento inserido é o primeiro a ser removido.
EX:
Pilha: [A, B, C]
- A é o primeiro elemento inserido, mas o último a ser removido.
- C é o último elemento inserido, mas o primeiro a ser removido.

'''
# ============================================================================

class Stack:
    """Implementação simples de pilha (LIFO) em Python."""

    def __init__(self):
        self._items = []

    def push(self, item):
        """Adiciona um item no topo da pilha."""
        self._items.append(item)

    def pop(self):
        """Remove e retorna o item do topo da pilha."""
        if self.is_empty():
            raise IndexError('A pilha está vazia')
        return self._items.pop()

    def peek(self):
        """Retorna o item do topo sem removê-lo."""
        if self.is_empty():
            raise IndexError('A pilha está vazia')
        return self._items[-1]

    def is_empty(self):
        """Verifica se a pilha está vazia."""
        return len(self._items) == 0

    def size(self):
        """Retorna o número de itens na pilha."""
        return len(self._items)

    def __repr__(self):
        return f'Pilha({self._items})'


if __name__ == '__main__':
    pilha = Stack()

    print('Criando uma pilha vazia...')
    print(pilha)

    print('\nInserindo itens: A, B, C')
    pilha.push('A')
    pilha.push('B')
    pilha.push('C')
    print('Pilha atual:', pilha)

    print('\nOlhar o topo sem remover:')
    print('Topo:', pilha.peek())

    print('\nRemovendo itens:')
    while not pilha.is_empty():
        print('Removido:', pilha.pop())
    print('Pilha vazia:', pilha.is_empty())
