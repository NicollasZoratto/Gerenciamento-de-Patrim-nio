from models.patrimonio import Patrimonio

class Equipamento(Patrimonio):
    def __init__(self, numero_patrimonio, descricao, localizacao, data_aquisicao, 
                 valor_aquisicao, categoria, vida_util):
        super().__init__(numero_patrimonio, descricao, localizacao, data_aquisicao, valor_aquisicao)
        self._categoria = categoria
        self._vida_util = vida_util
    
    def get_categoria(self):
        return self._categoria
    
    def set_categoria(self, categoria):
        self._categoria = categoria
    
    def get_vida_util(self):
        return self._vida_util
    
    def set_vida_util(self, vida_util):
        self._vida_util = vida_util
    
    def calcular_depreciacao(self):
        # Depreciação baseada na vida útil
        if self._vida_util > 0:
            return self._valor_aquisicao / self._vida_util
        return 0