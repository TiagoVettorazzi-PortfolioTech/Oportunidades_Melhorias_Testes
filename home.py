import streamlit as st
import main
import diagnostico_dir
import diagnostico_op

# Configuração inicial para controlar a navegação
if "current_page" not in st.session_state:
    st.session_state.current_page = "main"  # Página inicial definida como 'main'

# Função para navegar entre páginas
def navigate(page_name):
    st.session_state.current_page = page_name  # Atualiza a página atual
    st.rerun()  # Recarrega a aplicação para refletir a troca de página

# Renderiza a página com base no estado atual
def render_page():
    if st.session_state.current_page == "main":
        main.show(navigate)
    elif st.session_state.current_page == "diagnostico_dir":
        diagnostico_dir.show(navigate)
    elif st.session_state.current_page == "diagnostico_op":
        diagnostico_op.show(navigate)
    else:
        st.error("Página não encontrada!")  # Tratamento de erro para páginas desconhecidas

# Chama a função para renderizar a página atual
render_page()
