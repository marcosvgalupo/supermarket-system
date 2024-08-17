import datetime
from pagamento.Operadora import Operadora
from pagamento.PagamentoCartao import PagamentoCartao
from pagamento.PagamentoCheque import PagamentoCheque
from pagamento.PagamentoDinheiro import PagamentoDinheiro
from dominio.ItemVenda import ItemVenda

class Venda:
    def __init__(self):
        self.itensVenda = []
        self.estaCompleta = False
        self.data = datetime.datetime.now()
    def criar_item_venda(self, desc, quantidade):
        iv = ItemVenda(desc, quantidade)
        self.itensVenda.append(iv)

    def fazer_pagamento_dinheiro(self, quantiaFornecida):
        self.pagamento = PagamentoDinheiro(quantiaFornecida)
        return self.calcularTroco()

    def fazer_pagamento_cheque(self, quantiaFornecida, banco):
        self.pagamento = PagamentoCheque(quantiaFornecida, banco)

    def fazer_pagamento_cartao(self, quantiaFornecida, operadora, quantidadeParcelas, tipoCalculadora):
        self.pagamento = PagamentoCartao(quantiaFornecida, operadora, quantidadeParcelas, tipoCalculadora)

    def calcularTroco(self):
        return self.pagamento.get_quantia_fornecida() - self.calcular_total_venda()

    def calcular_total_venda(self):
        totalVenda = 0.0
        for itemVenda in self.itensVenda:
            if itemVenda is not None:
                totalVenda += itemVenda.get_descricao_produto().get_preco() * itemVenda.get_quantidade()
        return totalVenda

    def set_esta_completa(self, estaCompleta):
        self.estaCompleta = estaCompleta

    def __str__(self):
        status = "completa" if self.estaCompleta else "incompleta"
        dataTemp = self.data.strftime("%d/%m/%Y")
        horaTemp = self.data.strftime("%H:%M:%S")
        cabecalho = f"Data: {dataTemp} hora: {horaTemp}\n" \
            f"\t\t\t\t\tStatus da venda: {status}\n\n" \
            "Descrição\t\tPreço Unit"
        return cabecalho
