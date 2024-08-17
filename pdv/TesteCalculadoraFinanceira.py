from servicos import CalculadoraJurosCompostos, CalculadoraJurosSimples

montante_inicial = 10000
periodo_meses = 3
juros_ao_mes = 0.05

calculadora = CalculadoraJurosCompostos()
print("************* Cálculo de juros com calculadora de juros compostos **********************")
print("Montante inicial..:", montante_inicial)
print("Período em meses...:", periodo_meses)
print("Juros ao mês......: ", juros_ao_mes)
print("Objeto calculadora..:", calculadora)
print("Total..:", calculadora.calcularMontanteComJuros(montante_inicial, periodo_meses, juros_ao_mes))
print("*****************************************************")

calculadora = CalculadoraJurosSimples()
print("************* Cálculo de juros com calculadora de juros simples **********************")
print("Montante inicial..:", montante_inicial)
print("Período em meses...:", periodo_meses)
print("Juros ao mês......: ", juros_ao_mes)
print("Objeto calculadora..:", calculadora)
print("Total..:", calculadora.calcularMontanteComJuros(montante_inicial, periodo_meses, juros_ao_mes))
print("*****************************************************")
