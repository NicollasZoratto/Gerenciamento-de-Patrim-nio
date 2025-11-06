import streamlit as st
import pandas as pd
import sqlite3
from datetime import date
import os

# Configuração do banco de dados
def conectar_bd():
    return sqlite3.connect("Faculdade.db")

def criar_tabela():
    conn = conectar_bd()
    cursor = conn.cursor()
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
    conn.commit()
    conn.close()

# Inicializar banco
criar_tabela()

# Interface principal
st.title('🏛️ Sistema de Gerenciamento de Patrimônio - Faculdade')

menu = st.sidebar.selectbox("Menu", ["Incluir Patrimônio", "Consultar Patrimônio", "Excluir Patrimônio"])

if menu == "Incluir Patrimônio":
    st.header("📝 Cadastro de Patrimônio")
    
    numero_patrimonio = st.number_input("Número do Patrimônio:", min_value=1, step=1)
    descricao = st.text_input("Descrição:")
    tipo_patrimonio = st.selectbox("Tipo de Patrimônio", ["Computador", "Equipamento", "Móvel", "Outros"])
    localizacao = st.text_input("Localização:")
    data_aquisicao = st.date_input("Data de Aquisição:", value=date.today())
    valor_aquisicao = st.number_input("Valor de Aquisição (R$):", min_value=0.0, format="%.2f")
    estado_conservacao = st.selectbox("Estado de Conservação", ["Novo", "Bom", "Regular", "Precisa Manutenção"])
    
    if tipo_patrimonio == "Equipamento":
        vida_util = st.number_input("Vida Útil (anos):", min_value=1, step=1, value=5)
    else:
        vida_util = st.number_input("Vida Útil (anos):", min_value=1, step=1, value=10)
    
    if st.button("💾 Cadastrar Patrimônio", type="primary"):
        if not descricao:
            st.error("Por favor, preencha a descrição!")
        else:
            try:
                conn = conectar_bd()
                cursor = conn.cursor()
                
                cursor.execute("""
                INSERT INTO patrimonio 
                (numero_patrimonio, descricao, tipo, localizacao, data_aquisicao, valor_aquisicao, vida_util, estado_conservacao)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    int(numero_patrimonio),
                    descricao,
                    tipo_patrimonio,
                    localizacao,
                    data_aquisicao.strftime("%Y-%m-%d"),
                    float(valor_aquisicao),
                    vida_util,
                    estado_conservacao
                ))
                
                conn.commit()
                conn.close()
                st.success("✅ Patrimônio cadastrado com sucesso!")
                
            except sqlite3.IntegrityError:
                st.error("❌ Erro: Número de patrimônio já existe!")
            except Exception as e:
                st.error(f"❌ Erro ao cadastrar: {str(e)}")

elif menu == "Consultar Patrimônio":
    st.header("📊 Consulta de Patrimônio")
    
    if st.button("🔍 Consultar Todos os Patrimônios"):
        try:
            conn = conectar_bd()
            df = pd.read_sql_query("SELECT * FROM patrimonio ORDER BY numero_patrimonio", conn)
            conn.close()
            
            if not df.empty:
                st.subheader(f"📋 Patrimônios Encontrados: {len(df)} itens")
                
                # Calcular valor total
                valor_total = df['valor_aquisicao'].sum()
                st.metric("💰 Valor Total do Patrimônio", f"R$ {valor_total:,.2f}")
                
                # Mostrar tabela
                st.dataframe(df, use_container_width=True)
            else:
                st.info("ℹ️ Nenhum patrimônio cadastrado.")
                
        except Exception as e:
            st.error(f"❌ Erro ao consultar: {str(e)}")

elif menu == "Excluir Patrimônio":
    st.header("🗑️ Exclusão de Patrimônio")
    
    # Mostrar patrimônios existentes primeiro
    try:
        conn = conectar_bd()
        df = pd.read_sql_query("SELECT numero_patrimonio, descricao, tipo, localizacao FROM patrimonio ORDER BY numero_patrimonio", conn)
        conn.close()
        
        if not df.empty:
            st.subheader("Patrimônios Cadastrados")
            st.dataframe(df, use_container_width=True)
            
            st.subheader("Excluir Patrimônio")
            numero_excluir = st.number_input("Digite o número do patrimônio a excluir:", min_value=1, step=1)
            
            if st.button("❌ Excluir Patrimônio", type="secondary"):
                if numero_excluir in df['numero_patrimonio'].values:
                    try:
                        conn = conectar_bd()
                        cursor = conn.cursor()
                        cursor.execute("DELETE FROM patrimonio WHERE numero_patrimonio = ?", (int(numero_excluir),))
                        conn.commit()
                        conn.close()
                        st.success(f"✅ Patrimônio {numero_excluir} excluído com sucesso!")
                        st.rerun()
                    except Exception as e:
                        st.error(f"❌ Erro ao excluir: {str(e)}")
                else:
                    st.error("❌ Número de patrimônio não encontrado!")
        else:
            st.info("ℹ️ Nenhum patrimônio cadastrado.")
            
    except Exception as e:
        st.error(f"❌ Erro ao carregar patrimônios: {str(e)}")

# Rodapé
st.sidebar.markdown("---")
st.sidebar.markdown("**Sistema de Gestão Patrimonial**  \nFaculdade - 2025")