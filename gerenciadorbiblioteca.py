id_livro = 1
numero_membro = 1

class Livro:
    def __init__(self, titulo, id, autor) -> None:
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

class Membro:
    def __init__(self, nome, numero) -> None:
        self.nome = nome
        self.numero = numero
        self.historico = []


class Biblioteca:
    def __init__(self) -> None:
        self.catalogo_livros = []
        self.registro_membros = []
    
    def adicionar_livro(self):
        global id_livro
        titulo_livro = str(input("Digite o título do livro: "))
        autor_livro = str(input("Digite o autor do livro: "))

        livro = Livro(titulo=titulo_livro, autor=autor_livro, id=id_livro)
        id_livro += 1
        self.catalogo_livros.append(livro)

    def adicionar_membro(self):
        global numero_membro
        nome_membro = str(input("Digite o nome do membro: "))

        membro = Membro(nome=nome_membro, numero=numero_membro)
        numero_membro += 1
        self.registro_membros.append(membro)

    def emprestar_livro(self):
        membro_foi_encontrado = False
        livro_foi_encontrado = False
        membro_escolhido = str(input("Digite o Nome ou ID do membro que irá alugar o livro: "))
        for membro_atual in self.registro_membros:
            if membro_atual.nome == membro_escolhido or str(membro_atual.id) == membro_escolhido:
                membro_foi_encontrado = True
                livro_escolhido = str(input("Digite o título ou ID do livro que você quer: "))
                for livro_atual in self.catalogo_livros:
                    if livro_atual.titulo == livro_escolhido or str(livro_atual.id) == livro_escolhido and livro_atual.disponivel == True:
                        livro_foi_encontrado = True
                        livro_atual.disponivel = False
                        membro_atual.historico.append(livro_atual)
        if membro_foi_encontrado == False:
            return "Membro não encontrado"
        if livro_foi_encontrado == False:
            return "Livro não encontrado"
    
    def devolver_livro(self):
        livro_foi_encontrado = False
        livro_escolhido = str(input("Digite o título ou ID do livro que você quer: "))
        for livro_atual in self.catalogo_livros:
            if livro_atual.titulo == livro_escolhido or str(livro_atual.id) == livro_escolhido and livro_atual.disponivel == False:
                livro_foi_encontrado = True
                livro_atual.disponivel = True
        if livro_foi_encontrado == False:
            return "Livro não encontrado"

    def pesquisar_livro(self):
        pesquisa_do_livro = str(input("Digite o título ou autor ou ID do livro: "))

        for livro_atual in self.catalogo_livros:
            if livro_atual.titulo == pesquisa_do_livro or livro_atual.autor == pesquisa_do_livro or str(livro_atual.id) == pesquisa_do_livro:
                print(f"""
                Informações do livro:
                ID do livro: {livro_atual.id}
                Título do livro: {livro_atual.titulo}
                Autor do livro: {livro_atual.autor}
                Status do livro: {livro_atual.disponivel}
                """)



biblioteca1 = Biblioteca()

while True:
    menu = int(input("""
    Escolha uma opção:
    1 - Adicionar livro
    2 - Adicionar membro
    3 - Emprestar livro
    4 - Devolver livro
    5 - Pesquisar livros
    0 - Sair                
    """))

    match menu:
        case 1:
            print(biblioteca1.adicionar_livro())
        case 2:
            print(biblioteca1.adicionar_membro())
        case 3:
            print(biblioteca1.emprestar_livro())
        case 4:
           print(biblioteca1.devolver_livro())
        case 5:
            biblioteca1.pesquisar_livro()
        case 0:
            break
        case _:
            print("Opção inválida")