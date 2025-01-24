import streamlit as st
from diagnostico_dir import diagnostico_dir_app
from diagnostico_op import diagnostico_op_app

def main():
    st.set_page_config(page_title="Página Inicial", layout="wide")
    st.markdown("<h1 style='text-align: center; color: #AC8D61;'>Bem-vindo</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Escolha uma das opções abaixo para continuar:</p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Ir para Diagnóstico Dir"):
            st.session_state.current_flow = "dir"
            st.experimental_rerun()
    with col2:
        if st.button("Ir para Diagnóstico Op"):
            st.session_state.current_flow = "op"
            st.experimental_rerun()

    # Navegar para a aplicação escolhida
    if "current_flow" in st.session_state:
        if st.session_state.current_flow == "dir":
            diagnostico_dir_app()
        elif st.session_state.current_flow == "op":
            diagnostico_op_app()

if __name__ == "__main__":
    main()

