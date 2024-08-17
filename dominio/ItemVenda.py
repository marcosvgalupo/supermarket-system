class ItemVenda:
    def __init__(self, descricao_produto, quantidade):
        self.descricao_produto = descricao_produto
        self.quantidade = quantidade

    def get_quantidade(self):
        return self.quantidade

    def get_descricao_produto(self):
        return self.descricao_produto

    def get_subtotal(self):
        return self.quantidade * self.descricao_produto.get_preco()

    def __str__(self):
        return f"{str(self.descricao_produto)}\t    {self.quantidade}  \t\t{self.get_subtotal()}\n"
