class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node({self.value})"

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

if __name__ == "__main__":
    # Exemplo de uso
    # Criar uma árvore binária de busca e inserir alguns valores.
    bst = BinarySearchTree()
    bst.insert(5)  # raiz
    bst.insert(3)  # valor menor, vai para a esquerda
    bst.insert(7)  # valor maior, vai para a direita
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)

    # Buscar valores existentes e não existentes.
    valor_procura = 3
    resultado = bst.search(valor_procura)
    if resultado is not None:
        print(f"Valor {valor_procura} encontrado: {resultado.value}")
    else:
        print(f"Valor {valor_procura} não encontrado")

    valor_procura = 9
    resultado = bst.search(valor_procura)
    if resultado is not None:
        print(f"Valor {valor_procura} encontrado: {resultado.value}")
    else:
        print(f"Valor {valor_procura} não encontrado")

    # Verificar a estrutura básica da árvore.
    print(f"Raiz: {bst.root}")
    print(f"Filho esquerdo da raiz: {bst.root.left}")
    print(f"Filho direito da raiz: {bst.root.right}")   