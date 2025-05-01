import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="Sistema de Orçamento de Gravação - Prefeitura",
    page_icon="🎥",
    layout="wide",
)

# Título 
st.title("🎥 Sistema de Orçamento de Gravação")
st.subheader("Prefeitura Municipal Rosário do Ivaí")
st.markdown("---")


if 'orcamentos' not in st.session_state:
    st.session_state.orcamentos = pd.DataFrame(columns=[
        'Data', 'Nome', 'Contato', 'Tipo de Filmagem', 'Uso de Drone', 'Local', 'Status'
    ])


def salvar_orcamento(nome, contato, tipo_filmagem, uso_drone, local):
    novo_orcamento = pd.DataFrame({
        'Data': [datetime.now().strftime("%d/%m/%Y %H:%M")],
        'Nome': [nome],
        'Contato': [contato],
        'Tipo de Filmagem': [tipo_filmagem],
        'Uso de Drone': ["Sim" if uso_drone else "Não"],
        'Local': [local],
        'Status': ["Aguardando avaliação"]
    })
    
    st.session_state.orcamentos = pd.concat([st.session_state.orcamentos, novo_orcamento], ignore_index=True)


if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False
    
if 'senha_administrador' not in st.session_state:
    st.session_state.senha_administrador = "prefeitura123"  # SSENHA PARA ADMIN


if st.session_state.autenticado:
 
    tab1, tab2 = st.tabs(["Orçamentos Solicitados", "Sair"])
    
    with tab1:
        st.header("Painel Administrativo - Orçamentos Solicitados")
        
       
        if not st.session_state.orcamentos.empty:
            st.dataframe(st.session_state.orcamentos, use_container_width=True)
            
           
            csv = st.session_state.orcamentos.to_csv(index=False).encode('utf-8')
            st.download_button(
                "Baixar Relatório (CSV)",
                data=csv,
                file_name=f"orcamentos_gravacao_{datetime.now().strftime('%Y%m%d')}.csv",
                mime='text/csv',
            )
        else:
            st.info("Ainda não há orçamentos solicitados.")
    
    with tab2:
        if st.button("Sair do Modo Administrativo"):
            st.session_state.autenticado = False
            st.rerun()
else:
    
    tab1, tab2 = st.tabs(["Solicitar Orçamento", "Área Administrativa"])
    
    with tab1:
        
        with st.form("orcamento_form"):
            st.header("Solicitar Orçamento")
            
            
            st.subheader("Informações de Contato")
            nome = st.text_input("Nome completo")
            contato = st.text_input("Telefone/E-mail")
            
            
            st.subheader("Detalhes da Gravação")
            
            tipo_filmagem = st.selectbox(
                "Tipo de Filmagem", 
                ["Curto (até 30 min)", "Médio (30 min a 2 horas)", "Longo (mais de 2 horas)"]
            )
            
            uso_drone = st.checkbox("Gravação com Drone")
            
            local = st.selectbox(
                "Local de Gravação",
                ["Rosario do Ivai", "Campineiro", "Boa Vista", "Viagem Fora"]
            )
            
            st.markdown("*O orçamento será elaborado pela Prefeitura e enviado para seu contato em breve.*")
            
            
            submitted = st.form_submit_button("Solicitar Orçamento")
            
            if submitted:
                if nome and contato:
                    salvar_orcamento(nome, contato, tipo_filmagem, uso_drone, local)
                    st.success("Orçamento solicitado com sucesso! A Prefeitura entrará em contato em breve.")
                else:
                    st.error("Por favor, preencha seu nome e contato.")
    
    with tab2:
        st.header("Acesso Administrativo")
        st.write("Área restrita para funcionários da Prefeitura.")
        
        senha = st.text_input("Digite sua senha de acesso", type="password")
        if st.button("Acessar"):
            if senha == st.session_state.senha_administrador:
                st.session_state.autenticado = True
                st.success("Autenticação realizada com sucesso!")
                st.rerun()
            else:
                st.error("Senha incorreta. Acesso negado.")


st.markdown("---")
st.markdown("**Sistema de Orçamentos de Gravação para Prefeitura © 2025**")
st.markdown("Para mais informações, entre em contato com o departamento de comunicação.")