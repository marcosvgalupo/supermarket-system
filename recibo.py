from dominio.Endereco import Endereco
from dominio.Loja import Loja
from excecoes.DescricaoProdutoInexistente import DescricaoProdutoInexistente
from pagamento.Operadora import Operadora
from dominio.Registradora import Registradora
from dominio.TipoCalculadora import TipoCalculadora


def gerar_recibo(registradora, troco):
    venda = registradora.get_venda_corrente()
    print("")
    print("--------------------------- Supermercado Preço Bão ---------------------------")
    print("                             Registradora : " + registradora.get_id())
    print("\t\t\t\tCUPOM FISCAL")
    print(venda)
    print("Troco................: R$ " + str(troco))



endereco = Endereco("Rua X", "", 5, "Alfenas", "Aeroporto", "MG", "37130-000")
loja = Loja("Supermercado Preço Bão", endereco)

try:
    # Criando uma venda com cartão, uma parcela na primeira registradora
    # entrarItem de Registradora pode lançar uma exceção DescricaoProdutoInexistente
    registradora = loja.get_registradora("R01")
    registradora.criar_nova_venda()

    registradora.entrar_item("01", 3)
    registradora.entrar_item("02", 2)
    registradora.entrar_item("03", 1)

    registradora.finalizar_venda()

    # TODO troco como retorno de fazer pagamento?
    total_venda = registradora.get_venda_corrente().calcular_total_venda()
    registradora.fazer_pagamento_cartao(total_venda, Operadora.AMERICAN, 1, TipoCalculadora.JUROS_SIMPLES)

    # 0.0 é o troco a ser devolvido
    gerar_recibo(registradora, 0.0)

    # Criando uma venda com pagamento em dinheiro na segunda registradora
    registradora2 = loja.get_registradora("R02")
    registradora2.criar_nova_venda()

    registradora2.entrar_item("08", 3)
    registradora2.entrar_item("01", 2)
    registradora2.entrar_item("09", 1)

    registradora2.finalizar_venda()

    registradora2.fazer_pagamento_dinheiro(100.00)

    # troco (200 fornecidos - valor total da venda)
    gerar_recibo(registradora2, 100 - registradora2.get_venda_corrente().calcular_total_venda())

    # Criando uma venda com cheque na terceira registradora
    registradora3 = loja.get_registradora("R02")

    registradora3.criar_nova_venda()
    registradora3.entrar_item("06", 3)
    registradora3.entrar_item("07", 2)
    registradora3.entrar_item("02", 1)
    registradora3.finalizar_venda()
    registradora3.fazer_pagamento_cheque( (registradora3.get_venda_corrente().calcular_total_venda()), "Banco do Brasil")

    # 0.0 é o troco a ser devolvido
    gerar_recibo(registradora3, 0.0)

except DescricaoProdutoInexistente as d:
    print(d)
