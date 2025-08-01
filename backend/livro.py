class Livro:
    def __init__(self, id, titulo):
        self.id = id
        self.titulo = titulo
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return True
        return False

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            return True
        return False
