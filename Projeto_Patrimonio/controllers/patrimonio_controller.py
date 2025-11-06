import sqlite3
from models.computador import Computador
from models.equipamento import Equipamento
import services.database as db

def incluir_patrimonio(patrimonio):
    conexao = db.criar_conexao()
    cursor = conexao.cursor()
    
    try:
        if isinstance(patrimonio, Computador):
            cursor.execute("""
            INSERT INTO patrimonio (numero_patrimonio, descricao, tipo, localizacao, 
                                  data_aquisicao, valor_aquisicao, vida_util, estado_conservacao)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                patrimonio.get_numero_patrimonio(),
                patrimonio.get_descricao(),
                'Computador',
                patrimonio.get_localizacao(),
                patrimonio.get_data_aquisicao(),
                patrimonio.get_valor_aquisicao(),
                5,  # Vida útil padrão para computadores
                'Bom'  # Estado de conservação padrão
            ))
        
        elif isinstance(patrimonio, Equipamento):
            cursor.execute("""
            INSERT INTO patrimonio (numero_patrimonio, descricao, tipo, localizacao, 
                                  data_aquisicao, valor_aquisicao, vida_util, estado_conservacao)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                patrimonio.get_numero_patrimonio(),
                patrimonio.get_descricao(),
                'Equipamento',
                patrimonio.get_localizacao(),
                patrimonio.get_data_aquisicao(),
                patrimonio.get_valor_aquisicao(),
                patrimonio.get_vida_util(),
                'Bom'  # Estado de conservação padrão
            ))
        
        conexao.commit()
        print("Patrimônio inserido com sucesso!")
        return True
    
    except sqlite3.Error as e:
        print(f"Erro ao inserir patrimônio: {e}")
        return False
    finally:
        conexao.close()

def consultar_patrimonio():
    conexao = db.criar_conexao()
    cursor = conexao.cursor()
    
    try:
        cursor.execute('SELECT * FROM patrimonio')
        rows = cursor.fetchall()
        
        dados = []
        
        for row in rows:
            (numero_patrimonio, descricao, tipo, localizacao, 
             data_aquisicao, valor_aquisicao, vida_util, estado_conservacao) = row
            
            if tipo == 'Computador':
                patrimonio = Computador(numero_patrimonio, descricao, localizacao, 
                                      data_aquisicao, valor_aquisicao, '', '', '')
                depreciacao = patrimonio.calcular_depreciacao()
            elif tipo == 'Equipamento':
                patrimonio = Equipamento(numero_patrimonio, descricao, localizacao, 
                                       data_aquisicao, valor_aquisicao, '', vida_util)
                depreciacao = patrimonio.calcular_depreciacao()
            else:
                depreciacao = 0
            
            dados.append({
                "Número Patrimônio": numero_patrimonio,
                "Descrição": descricao,
                "Tipo": tipo,
                "Localização": localizacao,
                "Data Aquisição": data_aquisicao,
                "Valor Aquisição": valor_aquisicao,
                "Vida Útil": vida_util,
                "Estado Conservação": estado_conservacao,
                "Depreciação Anual": depreciacao
            })
        
        return dados
    
    except sqlite3.Error as e:
        print(f"Erro ao consultar patrimônio: {e}")
        return []
    finally:
        conexao.close()

def excluir_patrimonio(numero_patrimonio):
    try:
        conexao = db.criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM patrimonio WHERE numero_patrimonio = ?", (numero_patrimonio,))
        conexao.commit()
        print(f"Patrimônio com número {numero_patrimonio} excluído com sucesso!")
        return True
    except sqlite3.Error as e:
        print(f"Erro ao excluir patrimônio: {e}")
        return False
    finally:
        if conexao:
            conexao.close()