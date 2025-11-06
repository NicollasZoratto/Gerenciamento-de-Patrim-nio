from models.patrimonio import Patrimonio

class Computador(Patrimonio):
    def __init__(self, numero_patrimonio, descricao, localizacao, data_aquisicao, 
                 valor_aquisicao, processador, memoria_ram, armazenamento):
        super().__init__(numero_patrimonio, descricao, localizacao, data_aquisicao, valor_aquisicao)
        self._processador = processador
        self._memoria_ram = memoria_ram
        self._armazenamento = armazenamento
    
    def get_processador(self):
        return self._processador
    
    def set_processador(self, processador):
        self._processador = processador
    
    def get_memoria_ram(self):
        return self._memoria_ram
    
    def set_memoria_ram(self, memoria_ram):
        self._memoria_ram = memoria_ram
    
    def get_armazenamento(self):
        return self._armazenamento
    
    def set_armazenamento(self, armazenamento):
        self._armazenamento = armazenamento
    
    def calcular_depreciacao(self):
        # Depreciação linear de 20% ao ano para computadores
        return self._valor_aquisicao * 0.2