from dominio.Registradora import Registradora
from dominio.Venda import Venda


class Loja:

  def __init__(self, nome, endereco):
    self.nome = nome
    self.vendas = []
    self.registradoras = []
    self.endereco = endereco

    r1 = Registradora("R01")
    r2 = Registradora("R02")
    r3 = Registradora("R03")

    self.adicionar_registradora(r1)
    self.adicionar_registradora(r2)
    self.adicionar_registradora(r3)

  def adicionar_venda(self, v):  #Venda v
    self.vendas.append(v)

  def adicionar_registradora(self, registradora):
    self.registradoras.append(registradora)

  def get_ultima_venda(self):
    return self.vendas[-1]

  def get_registradora(self, id):
    for registradora in self.registradoras:
      if registradora.get_id() == id:
        return registradora
    return None

  def get_nome(self):
    return self.nome

  def set_nome(self, nome):
    self.nome = nome

  def get_endereco(self):
    return self.endereco

  def set_endereco(self, endereco):
    self.endereco = endereco
