import datetime
import tkinter as tk
from tkinter import ttk
from dominio.Registradora import Registradora
from dominio.Endereco import Endereco
from dominio.Loja import Loja
from servicos.CalculadoraJurosCompostos import CalculadoraJurosCompostos
from servicos.CalculadoraJurosSimples import CalculadoraJurosSimples

REGISTRADORA_ID = "R01"
SUPERMARKET_NAME = "Supermarket"
SUPERMARKET_ADRESS = Endereco("Rua X", "", 5, "Alfenas", "Aeroporto", "MG", "37130-000")
loja = Loja(SUPERMARKET_NAME, SUPERMARKET_ADRESS)  
registradora = loja.get_registradora(REGISTRADORA_ID)
catalogo = registradora.get_catalogo()
calcJS = CalculadoraJurosSimples()
calcJC = CalculadoraJurosCompostos()
global pagamento_atual
pagamento_atual = ""
  
def __init__(self, root):
  self.root = root
  self.root.title("Minha Aplicação")
  self.create_widgets()


def adicionar_item_a_compra():
  try:
    quantidade_itens = int(quantidade_textfield.get())
    id_do_item = item_id_textfield.get()
    registradora.entrar_item(id_do_item, quantidade_itens)
    produto = catalogo.get_descricao_produto(id_do_item)
    for _ in range(quantidade_itens):
      carrinho_item_listview.insert(tk.END, f"{produto.get_descricao()}, {produto.get_preco()}")
      carrinho_item_listview.update()
  except ValueError:
    pass
    

def finalizar_venda():
    exibir_total_carrinho()
    desabilitar_elemento(adicionar_item_button)
    desabilitar_elemento(quantidade_textfield)
    desabilitar_elemento(item_id_textfield)
    pass

def criar_nova_venda():
  limpaCarrinho()
  habilitar_elemento(adicionar_item_button)
  habilitar_elemento(quantidade_textfield)
  habilitar_elemento(item_id_textfield)
  habilitar_elemento(operadora_dropbox)
  habilitar_elemento(juros_dropbox)
  habilitar_elemento(quantidade_parcelas_textfield)
  habilitar_elemento(banco_textfield)
  habilitar_elemento(valor_fornecido_textfield)
  habilitar_elemento(pagamento_dropbox)
  registradora.criar_nova_venda()


def exibir_total_carrinho():
  total_carrinho = 0.0
  for i in range(carrinho_item_listview.size()):
     item = carrinho_item_listview.get(i)
     item_price = (float)(item.split(",")[1])
     total_carrinho += item_price
  valor_total_var.set(total_carrinho)
  return total_carrinho

def limpaCarrinho():
   carrinho_item_listview.delete(0, tk.END)
   quantidade_textfield.delete(0, tk.END)
   item_id_textfield.delete(0, tk.END)

 
  
def desabilitar_elemento(elemento):
    elemento["state"] = "disable"

def habilitar_elemento(elemento):
    elemento["state"] = "normal"

def fazer_pagamento():
    global pagamento_atual
    if pagamento_dropbox.get() == "Dinheiro":
       habilitar_elemento(valor_fornecido_textfield)
       desabilitar_elemento(banco_textfield)
       desabilitar_elemento(operadora_dropbox)
       desabilitar_elemento(juros_dropbox)
       desabilitar_elemento(quantidade_parcelas_textfield)
       pagamento_atual = "Dinheiro"
    elif pagamento_dropbox.get() == "Cheque":
       habilitar_elemento(banco_textfield)
       desabilitar_elemento(operadora_dropbox)
       desabilitar_elemento(juros_dropbox)
       desabilitar_elemento(quantidade_parcelas_textfield)
       pagamento_atual = "Cheque"
    else:
       habilitar_elemento(operadora_dropbox)
       habilitar_elemento(juros_dropbox)
       habilitar_elemento(quantidade_parcelas_textfield)
       desabilitar_elemento(banco_textfield)
       desabilitar_elemento(valor_fornecido_textfield)
       pagamento_atual = "Cartão"

def calcular_juros():
   if juros_dropbox.get() == "JUROS_SIMPLES":
    qp = (int)(quantidade_parcelas_textfield.get())
    total = exibir_total_carrinho()
    valor = calcJS.calcularMontanteComJuros(total, qp, 5)
    return valor
   else:
    qp = (int)(quantidade_parcelas_textfield.get())
    total = exibir_total_carrinho()
    valor = calcJC.calcularMontanteComJuros(total, qp, 5)
    return valor

def gerar_recibo():
   global pagamento_atual
   print(pagamento_atual)
   if pagamento_atual == "Dinheiro":
      data = datetime.date.today().strftime("%d/%m/%Y")
      fornecido = (int)(valor_fornecido_textfield.get())
      t_fornecido = fornecido - exibir_total_carrinho()
      novo_texto = f"Data: {data}\nStatus da Venda: Concluída \nValor Fornecido: R$ {fornecido}\nTroco: R$ {t_fornecido}"
      recibo_var.set(novo_texto)
   elif pagamento_atual == "Cheque":
      data = datetime.date.today().strftime("%d/%m/%Y")
      fornecido = valor_fornecido_textfield.get()
      novo_texto = f"Data: {data}\nStatus da Venda: Concluída \nValor Fornecido: R$ {fornecido}\nBanco: {banco_textfield.get()}"
      recibo_var.set(novo_texto)
   elif pagamento_atual == "Cartão":
      data = datetime.date.today().strftime("%d/%m/%Y")
      fornecido = exibir_total_carrinho()
      stringCartao = f"\nParcelas: {quantidade_parcelas_textfield.get()} \nOperadora: {operadora_dropbox.get()}\nJuros Ao Mês: 0.05"
      tipoJuros = f"\nTipo do Juros: {juros_dropbox.get()} \nValor total da compra: R$ {calcular_juros()}"
      novo_texto = f"Data: {data}\nStatus da Venda: Concluída \nValor da Compra: R$ {fornecido}" + stringCartao + tipoJuros
      recibo_var.set(novo_texto)
      

def realizar_pagamento():
  gerar_recibo()
  desabilitar_elemento(operadora_dropbox)
  desabilitar_elemento(juros_dropbox)
  desabilitar_elemento(quantidade_parcelas_textfield)
  desabilitar_elemento(banco_textfield)
  desabilitar_elemento(valor_fornecido_textfield)
  desabilitar_elemento(pagamento_dropbox)



root = tk.Tk()
root.title("Supermercado Preço Bão")
root.geometry("800x600")

# Main Frame
main_frame = ttk.Frame(root)
main_frame.pack(pady=20, padx=20)

# Menu Box
menu_box = ttk.LabelFrame(main_frame, text="Menu", padding=(20, 20))
menu_box.grid(row=0, column=0, padx=10, sticky="n")

item_id_label = ttk.Label(menu_box, text="Id do Item:")
item_id_label.grid(row=0, column=0, padx=5, pady=5)
item_id_textfield = ttk.Entry(menu_box)
item_id_textfield.grid(row=0, column=1, padx=5, pady=5)

quantidade_label = ttk.Label(menu_box, text="Quantidade:")
quantidade_label.grid(row=0, column=2, padx=5, pady=5)
quantidade_textfield = ttk.Entry(menu_box)
quantidade_textfield.grid(row=0, column=3, padx=5, pady=5)

adicionar_item_button = ttk.Button(menu_box, text="Adicionar Item", command=adicionar_item_a_compra)
adicionar_item_button.grid(row=0, column=4, padx=5, pady=5)

carrinho_item_listview = tk.Listbox(menu_box, height=15)
carrinho_item_listview.grid(row=1, column=0, columnspan=5, padx=5, pady=5)

finalizar_compra_button = ttk.Button(menu_box, text="Finalizar Compra", command=finalizar_venda)
finalizar_compra_button.grid(row=2, column=3, padx=5, pady=5)

nova_compra_button = ttk.Button(menu_box, text="Iniciar Nova Compra", command=criar_nova_venda)
nova_compra_button.grid(row=2, column=4, padx=5, pady=5)

botao_calcular = ttk.Button(menu_box, text="Calcular Total", command=exibir_total_carrinho)
botao_calcular.grid(row=2, column=0, padx=5, pady=5)

global valor_total_var
valor_total_var = tk.StringVar()
total_a_pagar = ttk.Label(menu_box, textvariable=valor_total_var)
total_a_pagar.grid(row=2, column=1, padx=5, pady=5)

# Receipt Box
receipt_box = ttk.LabelFrame(main_frame, text="Cupom Fiscal", padding=(20, 20))
receipt_box.grid(row=0, column=1, padx=10, sticky="n")

receipt_label = ttk.Label(receipt_box, text="--------------------------- Supermercado Preço Bão ---------------------------")
receipt_label.pack()

recibo_box = ttk.Frame(receipt_box)
recibo_box.pack(pady=10, padx=10)

global recibo_var
recibo_var = tk.StringVar()

recibo_venda_label = ttk.Label(recibo_box, textvariable=recibo_var)
recibo_venda_label.pack()


# Payment Box
pagamento_box = ttk.LabelFrame(root, text="Pagamento", padding=(20, 20))
pagamento_box.pack(pady=20, padx=20)

forma_pagamento_label = ttk.Label(pagamento_box, text="Forma de pagamento:")
forma_pagamento_label.grid(row=0, column=0, padx=5, pady=5)

pagamento_dropbox = ttk.Combobox(pagamento_box, values=["Dinheiro", "Cheque", "Cartão"])
pagamento_dropbox.grid(row=0, column=1, padx=5, pady=5)
pagamento_dropbox.bind("<<ComboboxSelected>>", lambda event: fazer_pagamento())

valor_fornecido_label = ttk.Label(pagamento_box, text="Valor fornecido em R$:")
valor_fornecido_label.grid(row=1, column=0, padx=5, pady=5)

valor_fornecido_textfield = ttk.Entry(pagamento_box)
valor_fornecido_textfield.grid(row=1, column=1, padx=5, pady=5)

banco_label = ttk.Label(pagamento_box, text="Banco:")
banco_label.grid(row=2, column=0, padx=5, pady=5)

banco_textfield = ttk.Entry(pagamento_box)
banco_textfield.grid(row=2, column=1, padx=5, pady=5)

operadora_label = ttk.Label(pagamento_box, text="Operadora:")
operadora_label.grid(row=3, column=0, padx=5, pady=5)

operadora_dropbox = ttk.Combobox(pagamento_box, values=["VISA", "MASTERCARD", "AMERICAN", "DINNERS"])
operadora_dropbox.grid(row=3, column=1, padx=5, pady=5)

parcelas_label = ttk.Label(pagamento_box, text="Parcelas:")
parcelas_label.grid(row=4, column=0, padx=5, pady=5)

quantidade_parcelas_textfield = ttk.Entry(pagamento_box)
quantidade_parcelas_textfield.grid(row=4, column=1, padx=5, pady=5)

juros_label = ttk.Label(pagamento_box, text="Juros:")
juros_label.grid(row=5, column=0, padx=5, pady=5)

juros_dropbox = ttk.Combobox(pagamento_box, values=["JUROS_SIMPLES", "JUROS_COMPOSTOS"])
juros_dropbox.grid(row=5, column=1, padx=5, pady=5)

# Finalizar Compra Button
finalizar_compra_button = ttk.Button(pagamento_box, text="Finalizar Compra", command=finalizar_venda)
finalizar_compra_button.grid(row=6, column=1, padx=5, pady=10, sticky="e")

realizar_pagamento_button = ttk.Button(pagamento_box, text="Realizar Pagamento", command=realizar_pagamento)
realizar_pagamento_button.grid(row=2, column=3)

criar_nova_venda()
root.mainloop()

