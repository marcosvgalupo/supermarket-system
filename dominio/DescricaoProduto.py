class DescricaoProduto:
    def __init__(self, id, preco, descricao):
        self.id = id
        self.preco = preco
        self.descricao = descricao

    def get_id(self):
        return self.id

    def get_preco(self):
        return self.preco

    def __str__(self):
        return f"{self.descricao}\t\t{self.preco}\t"
    
    def get_descricao(self):
        return self.descricao

    def __eq__(self, other):
        if isinstance(other, DescricaoProduto) and other is not None:
            return self.id == other.get_id()
        return False
