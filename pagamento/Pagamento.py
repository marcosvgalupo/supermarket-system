from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, quantia_fornecida):
        self.quantia_fornecida = quantia_fornecida

    def get_quantia_fornecida(self):
        return self.quantia_fornecida
    
    def set_quantia_fornecida(self, quantia):
        self.quantia_fornecida = quantia
    
    @abstractmethod
    def __str__(self):
        return "Quantia Fornecida: R$ " + str(self.quantia_fornecida)


