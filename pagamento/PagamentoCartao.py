from dominio.TipoCalculadora import TipoCalculadora
from servicos.CalculadoraJurosSimples import CalculadoraJurosSimples
from servicos.CalculadoraJurosCompostos import CalculadoraJurosCompostos
from servicos.IJuros import IJuros
from pagamento.Pagamento import Pagamento

class PagamentoCartao(Pagamento, IJuros):
    def __init__(self, quantia, operadora, quantidade_parcelas, tipo_calculadora):
        super().__init__(quantia)
        self.operadora = operadora
        self.quantidade_parcelas = quantidade_parcelas
        
        if tipo_calculadora == TipoCalculadora.JUROS_SIMPLES:
            self.calculadora = CalculadoraJurosSimples()
        elif tipo_calculadora == TipoCalculadora.JUROS_COMPOSTOS:
            self.calculadora = CalculadoraJurosCompostos()
    
    def simular_parcelas(self, quantia, quantidade_parcelas):
        juros = self.consultar_taxa_juros()
        montante_com_juros = self.calculadora.calcular_montante_com_juros(quantia, quantidade_parcelas, juros)
        return montante_com_juros / quantidade_parcelas
    
    def consultar_taxa_juros(self):
        taxa_juros = 0.0
        if self.quantidade_parcelas == 2:
            taxa_juros = 2.5
        elif self.quantidade_parcelas == 3:
            taxa_juros = 5.0
        return taxa_juros
    
    def __str__(self):
        return "Tipo de pagamento...: Cartão de Crédito\n" \
               + super().__str__() + "\n" \
               + "Operadora................: " + self.operadora + "\n" \
               + "Quantidade de parcelas....: " + str(self.quantidade_parcelas) + "\n" \
               + "Valor de cada parcela...: " + str(self.simular_parcelas(super().get_quantia_fornecida(), self.quantidade_parcelas)) + "\n" \
               + "Tipo de calculadora usada na transação................: " + str(self.calculadora) + "\n"
