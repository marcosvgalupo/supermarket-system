from dominio.Endereco import Endereco
from dominio.Loja import Loja


class HelloController:
  REGISTRADORA_ID = "R01"
  SUPERMARKET_NAME = "Supermarket"
  SUPERMARKET_ADRESS = Endereco("Rua X", "", 5, "Alfenas", "Aeroporto", "MG", "37130-000")
  loja = Loja(SUPERMARKET_NAME, SUPERMARKET_ADRESS)  
  registradora = loja.get_registradora(REGISTRADORA_ID)
  catalogo = registradora.get_catalogo()

  def desabilitarBotao(self, botao):
    botao["state"] = "disable"

  def habilitarBotao(self, botao):
    botao["state"] = "normal"

  def criarNovaVenda(self):
    limparCarrinho()
    #habilita botão de finalizar compra
    self.registradora.criar_nova_venda()
    totalAPagar(registradora.get_venda_corrente().calcularTotalVenda())
    
    
    
  def totalAPagar(self, valorTotal):
    valor = f"total: R$ {valorTotal}"
    
    
    
  