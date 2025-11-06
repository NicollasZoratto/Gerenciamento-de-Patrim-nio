import sqlite3

def criar_conexao():
    conexao = sqlite3.connect("Faculdade.db")
    return conexao

def criar_tabela_patrimonio():
    conexao = criar_conexao()
    cursor = conexao.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patrimonio (
        numero_patrimonio INTEGER PRIMARY KEY,
        descricao TEXT NOT NULL,
        tipo TEXT NOT NULL,
        localizacao TEXT,
        data_aquisicao TEXT,
        valor_aquisicao REAL,
        vida_util INTEGER,
        estado_conservacao TEXT
    )
    """)
    
    conexao.commit()
    conexao.close()
    print("Tabela PATRIMONIO criada com sucesso!")

# Criar a tabela ao importar este módulo
criar_tabela_patrimonio()