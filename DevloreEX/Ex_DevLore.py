class Livros:
    def __init__(self, nome, autor, isbn):
        self.nome = nome
        self.autor = autor
        self.isbn = isbn
    
    def livro_info(self):
        return f"Nome: {self.nome}, Autor: {self.autor}, ISBN: {self.isbn}"
            

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        if livro not in self.livros:
            self.livros.append(livro)
        else:
            print(f"O livro '{livro.nome}' já está na biblioteca.")

    def remover_livro(self, livro):
        if livro in self.livros:
            self.livros.remove(livro)
        else:
            print(f"O livro '{livro.nome}' não está na biblioteca.")

    def listar_livros(self):
        if not self.livros:
            print("A biblioteca está vazia.")
        else:
            print("Livros na biblioteca:")
            for livro in self.livros:
                print(f"- {livro.nome} por {livro.autor} (ISBN: {livro.isbn})")

    def buscar_livro_por_nome(self, nome):
        for livro in self.livros:
            if livro.nome.lower() == nome.lower():
                return livro.livro_info()
        return "Livro não encontrado."


livro_gatos = Livros("Gatos: Guia Completo", "John Doe", "1234567890")
livro_cachorros = Livros("Cachorros: Guia Completo", "Jane Smith", "0987654321")

biblioteca = Biblioteca()
biblioteca.adicionar_livro(livro_gatos) 
biblioteca.adicionar_livro(livro_cachorros)
