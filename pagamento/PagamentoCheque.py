from pagamento.Pagamento import Pagamento


class PagamentoCheque(Pagamento):

  def __init__(self, quantiaFornecida, banco):
    super().__init__(quantiaFornecida)
    self.banco = banco

  def getBanco(self):
    return self.banco

  def setBanco(self, banco):
    self.banco = banco

  def __str__(self):
    return f"Tipo de pagamento...: Cheque\n" \
           f"Quantia fornecida....: R$ {super().get_quantia_fornecida()}\n" \
           f"Banco................: {self.banco}"
