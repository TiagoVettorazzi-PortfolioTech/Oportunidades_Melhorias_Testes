# import streamlit as st

# # Função para exibir o conteúdo da Home
# def display_content():
#     st.title("Página Inicial")
#     st.write("Bem-vindo à página inicial!")
    
#     # Botão para iniciar o app1
#     if st.button("Iniciar App1"):
#         st.session_state.current_page = 0  # Página '🔍 Oportunidade de melhorias1' (app1)
#         st.rerun()
    
#     # Botão para iniciar o app2
#     if st.button("Iniciar App2"):
#         st.session_state.current_page = 1  # Página '🔍 Oportunidade de melhorias2' (app2)
#         st.rerun()


# app.py - Página central
import streamlit as st
from home import render_home
from app1 import render_app1
from app2 import render_app2

def main():
    st.set_page_config(page_title="Navegação Modular", layout="wide")
    
    # Configuração inicial
    if "current_page" not in st.session_state:
        st.session_state.current_page = "home"

    # Header de navegação na página principal
    st.title("Navegação entre Páginas")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Home"):
            st.session_state.current_page = "home"
    with col2:
        if st.button("App 1"):
            st.session_state.current_page = "app1"
    with col3:
        if st.button("App 2"):
            st.session_state.current_page = "app2"

    # Renderizar página selecionada
    if st.session_state.current_page == "home":
        render_home()
    elif st.session_state.current_page == "app1":
        render_app1()
    elif st.session_state.current_page == "app2":
        render_app2()

if __name__ == "__main__":
    main()










# import base64
# from pathlib import Path
# import streamlit as st


# def add_bg_from_local(image_file):
#     with Path(image_file).open("rb") as file:
#         encoded_string = base64.b64encode(file.read()).decode()
#     st.markdown(
#         f"""
#         <style>
#         .stApp {{
#             background-image: url(data:image/png;base64,{encoded_string});
#             background-size: cover;
#             background-position: center;
#             background-repeat: no-repeat;
#         }}
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# add_bg_from_local('background.png')

# st.markdown("""
#     <style>
#     /* Estilo para o título (h1) */
#     h1 {
#         font-size: 36px;
#         color: #0D47A1; /* Azul escuro para o título */
#     }
#     # /* Estilo para o subtítulo (h2) */
#     p {
#         font-size: 18px;
#         color: #000000; /* Cor para o subtítulo */
#     }

#     /* Estiliza botões do Streamlit */
#     div.stButton > button {
#         background-color: #007199; /* Fundo azul */
#         color: white; /* Texto branco */
#         border: none; /* Remover borda */
#         border-radius: 15px; /* Bordas arredondadas */
#         padding: 10px 20px; /* Espaçamento interno */
#         font-size: 16px; /* Tamanho do texto */
#         font-weight: bold; /* Texto em negrito */
#         cursor: pointer; /* Alterar cursor para ponteiro */
#         width: 200px;
#     }
#     div.stButton > button:hover {
#         background-color: #005f73; /* Fundo mais escuro ao passar o mouse */
#     }
#     .image-container {
#         display: flex;
#         justify-content: center;
#         align-items: center;
#         margin-top: 20px;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # Título da página
# st.markdown("<h1>Health Analyzer</h1>", unsafe_allow_html=True)

# # Texto de boas-vindas e subtítulo
# st.markdown("<h2>Bem-vindo ao seu <span style='color:#0D47A1;'>Health Analyzer</span></h2>", unsafe_allow_html=True)
# st.markdown("<p>Otimize seu pronto atendimento iniciando sua triagem do local onde você estiver.</p>", unsafe_allow_html=True)


# col1, col2, col3 = st.columns([3, 1, 3])
# with col1:
# # Botão de login que, ao clicar, navega para a página 'welcome'
#     st.button("Gerar Oportunidades")
# with col3:        
#     st.button("Detalhar Oportunidades")
