from abc import ABC, abstractmethod

class Patrimonio(ABC):
    def __init__(self, numero_patrimonio, descricao, localizacao, data_aquisicao, valor_aquisicao):
        self._numero_patrimonio = numero_patrimonio
        self._descricao = descricao
        self._localizacao = localizacao
        self._data_aquisicao = data_aquisicao
        self._valor_aquisicao = valor_aquisicao
    
    def get_numero_patrimonio(self):
        return self._numero_patrimonio
    
    def set_numero_patrimonio(self, numero_patrimonio):
        self._numero_patrimonio = numero_patrimonio
    
    def get_descricao(self):
        return self._descricao
    
    def set_descricao(self, descricao):
        self._descricao = descricao
    
    def get_localizacao(self):
        return self._localizacao
    
    def set_localizacao(self, localizacao):
        self._localizacao = localizacao
    
    def get_data_aquisicao(self):
        return self._data_aquisicao
    
    def set_data_aquisicao(self, data_aquisicao):
        self._data_aquisicao = data_aquisicao
    
    def get_valor_aquisicao(self):
        return self._valor_aquisicao
    
    def set_valor_aquisicao(self, valor_aquisicao):
        self._valor_aquisicao = valor_aquisicao
    
    @abstractmethod
    def calcular_depreciacao(self):
        pass