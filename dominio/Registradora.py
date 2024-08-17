from excecoes.DescricaoProdutoInexistente import DescricaoProdutoInexistente
from pagamento.Operadora import Operadora
from dominio.Venda import Venda
from dominio.CatalogoProdutos import CatalogoProdutos
from datetime import datetime


class Registradora:

  def __init__(self, id):
    self.id = id
    self.vendas = []
    self.catalogo = CatalogoProdutos()

  def criar_nova_venda(self):
    venda = Venda()
    self.vendas.append(venda)

  def entrar_item(self, id, quantidade):
    venda = None
    try:
      descricao_produto = self.catalogo.get_descricao_produto(id)
      venda = self.get_venda_corrente()
      venda.criar_item_venda(descricao_produto, quantidade)
    except DescricaoProdutoInexistente as e:
      print(e)

  def finalizar_venda(self):
    venda_corrente = self.get_venda_corrente()
    venda_corrente.set_esta_completa(True)

  def fazer_pagamento_dinheiro(self, quantia_fornecida):
    venda_corrente = self.get_venda_corrente()
    return venda_corrente.fazer_pagamento_dinheiro(quantia_fornecida)

  def fazer_pagamento_cheque(self, quantia_fornecida, banco):
    venda_corrente = self.get_venda_corrente()
    venda_corrente.fazer_pagamento_cheque(quantia_fornecida, banco)

  def fazer_pagamento_cartao(self, quantia_fornecida, operadora,quantidade_parcelas, tipo_calculadora):
    venda_corrente = self.get_venda_corrente()
    venda_corrente.fazer_pagamento_cartao(quantia_fornecida, operadora, quantidade_parcelas, tipo_calculadora)

  def get_venda_corrente(self):
    return self.vendas[-1]

  def get_catalogo(self):
    return self.catalogo

  def set_catalogo(self, catalogo):
    self.catalogo = catalogo

  def get_id(self):
    return self.id
