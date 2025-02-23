#Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.

#Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.

#Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.

#Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.

#Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.

#No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.

#No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.

#Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da classe Livro e exiba a mensagem formatada utilizando o método str.

class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    def __str__(self):
        return f'Título: {self.titulo}\nAutor: {self.autor}\nPublicação: {self.ano_publicacao}\nDisponível: {self.disponivel}'
    
    def emprestar(self):
        if self.disponivel == True:
            self.disponivel = False
    
    @staticmethod
    def verificar_disponibilidade(ano):
        if ano_publicação == ano:
        
livro_harrypotter = Livro('Harry Potter', 'JK Rolling', 1997)
livro_senhordosaneis = Livro('Senhor dos Aneis', 'J. R. R. Tolkien', 2001)

livro_senhordosaneis.emprestar()


print(livro_senhordosaneis)