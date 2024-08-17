class Endereco:
    def __init__(self, logradouro, complemento, numero, cidade, bairro, uf, cep):
        self.logradouro = logradouro
        self.complemento = complemento
        self.numero = numero
        self.cidade = cidade
        self.bairro = bairro
        self.uf = uf
        self.cep = cep

    def get_logradouro(self):
        return self.logradouro

    def set_logradouro(self, logradouro):
        self.logradouro = logradouro

    def get_complemento(self):
        return self.complemento

    def set_complemento(self, complemento):
        self.complemento = complemento

    def get_numero(self):
        return self.numero

    def set_numero(self, numero):
        self.numero = numero

    def get_cidade(self):
        return self.cidade

    def set_cidade(self, cidade):
        self.cidade = cidade

    def get_bairro(self):
        return self.bairro

    def set_bairro(self, bairro):
        self.bairro = bairro

    def get_uf(self):
        return self.uf

    def set_uf(self, uf):
        self.uf = uf

    def get_cep(self):
        return self.cep

    def set_cep(self, cep):
        self.cep = cep
