class DescricaoProdutoInexistente(Exception):
    def __init__(self, mensagem=None, id=None):
        super().__init__(mensagem)
        self.id = id

    def __str__(self):
        return super().__str__() + "\n" + f"ID....: {str(self.id)}"

