class CalculadoraJurosCompostos: #implements calculadoraFinanceira
  
  def calcularMontanteComJuros(self, montante_inicial, periodoMeses, jurosAoMes):
    novoMontante = montante_inicial * pow((1 + jurosAoMes), periodoMeses)
    return novoMontante

  def __str__(self):
    return "Calculadora de Juros Compostos"

