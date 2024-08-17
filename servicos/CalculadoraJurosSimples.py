class CalculadoraJurosSimples: #implements calculadoraFinanceira
 
  
  def calcularMontanteComJuros(self, montante_inicial, periodoMeses, jurosAoMes):
    totalJuros = montante_inicial * periodoMeses * (jurosAoMes * 0.01)
    novoMontante = montante_inicial + totalJuros
    return novoMontante;

  def __str__(self):
    return "Calculadora de Juros Simples"
