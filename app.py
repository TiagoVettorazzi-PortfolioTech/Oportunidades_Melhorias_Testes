# import streamlit as st
# import base64
# from pathlib import Path
# import os
# from dotenv import load_dotenv
# from process import run_agent_analysis  
# import pandas as pd
# from io import BytesIO
# import time
# import streamlit as st

# load_dotenv()
# api_key = os.getenv("OPENAI_API_KEY")

# all_resultados=[]

# if 'oportunidade' not in st.session_state:
#     st.session_state.oportunidades = []

# def stylable_container(key, css_styles):
#     st.markdown(f"""
#         <style>
#         div[data-testid="stHorizontalBlock"] > div:nth-child({key}) {{
#             {css_styles}
#         }}
#         </style>
#     """, unsafe_allow_html=True)
#     return st.container()

# # Colocando imagem de fundo
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

# def load_css(css_file):
#     with open(css_file, "r") as f:
#         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# # Estilização de botões
# def get_button_style(button_class):
#     if button_class == "current":
#         return "background-color: #01374C; color: white; font-weight: bold; font-size: 24px;"
#     elif button_class == "previous":
#         return "background-color: #4B4843; color: white; font-weight: normal; font-size: 24px;"
#     else:
#         return "background-color: #4B484340; color: #333333; font-size: 18px;"

# # Sidebar e navegação entre páginas
# def setup_navigation():
#     st.sidebar.markdown("<h1 style='text-align: center; color: #AC8D61;'>Navegação</h1>", unsafe_allow_html=True)
    
#     pages = ["🔍 Oportunidade de melhorias", "📋 Planilha Final"]
    
#     if 'current_page' not in st.session_state:
#         st.session_state.current_page = 0

#     for i, page in enumerate(pages):
#         button_class = "current" if i == st.session_state.current_page else "previous" if i == st.session_state.current_page - 1 else ""

#         if st.sidebar.button(page, key=f"nav_{i}", use_container_width=True, disabled=(i == st.session_state.current_page)):
#             st.session_state.current_page = i
#             st.rerun()

#         st.markdown(f"""
#             <style>
#             div.row-widget.stButton > button[key="nav_{i}"] {{
#                 {get_button_style(button_class)}
#             }}
#             </style>
#             """, unsafe_allow_html=True)

#     return pages

# # Adicionando oportunidade
# def add_oportunidade(new_oportunidade):
#     if new_oportunidade and new_oportunidade not in st.session_state.oportunidades:
#         st.session_state.oportunidades.append(new_oportunidade)
#         return True
#     return False

# # Removendo oportunidade
# def remove_oportunidade(oportunidade_to_remove):
#     if oportunidade_to_remove in st.session_state.oportunidades:
#         st.session_state.oportunidades.remove(oportunidade_to_remove)

# # Função para gerar excel
# def convert_df_to_excel(df):
#     output = BytesIO()
#     with pd.ExcelWriter(output, engine='openpyxl') as writer:
#         df.to_excel(writer, sheet_name='Oportunidade de melhorias', index=False)
#         for column in df:
#             column_width = max(df[column].astype(str).map(len).max(), len(column))
#             col_idx = df.columns.get_loc(column)
#             writer.sheets['Oportunidade de melhorias'].column_dimensions[chr(65 + col_idx)].width = column_width + 2
#     return output.getvalue()


# def render_diagnostico():
#     if 'form_inputs' not in st.session_state:
#         st.session_state.form_inputs = {
#             'ramo_empresa': '',
#             'nome_processo': '',
#             'atividade': '',
#             'evento': '',
#             'causa': ''
#         }
    
#     if 'all_resultados' not in st.session_state:
#         st.session_state.all_resultados = []
        
#     st.write("## Oportunidade de Melhoria")

#     with st.form(key='add_oportunidade_form'):
#         new_oportunidade = st.text_input(
#             "Novo oportunidade",
#             placeholder="Digite um novo oportunidade",
#             key="new_oportunidade"
#         )
#         if st.form_submit_button("Adicionar oportunidade"):
#             if add_oportunidade(new_oportunidade):
#                 st.success(f"oportunidade '{new_oportunidade}' adicionado com sucesso!")
#                 st.rerun()
#             else:
#                 if not new_oportunidade:
#                     st.warning("Por favor, digite um oportunidade.")
#                 else:
#                     st.warning("Este oportunidade já existe.")

#     for oportunidade in st.session_state.oportunidades:
#         col1, col2 = st.columns([3, 1])
#         with col1:
#             st.text(oportunidade)
#         with col2:
#             if st.button("Remover", key=f"remove_{oportunidade}"):
#                 remove_oportunidade(oportunidade)
#                 st.rerun()

#     with st.form(key='oportunidade_melhoria_form'):
#         ramo_empresa = st.text_input(
#             "Ramo da empresa", 
#             value=st.session_state.form_inputs['ramo_empresa'],
#             placeholder="Digite o ramo da empresa"
#         )
#         nome_processo = st.text_input(
#             "Nome do processo", 
#             value=st.session_state.form_inputs['nome_processo'],
#             placeholder="Digite o nome do processo"
#         )
#         atividade = st.text_input(
#             "Atividade", 
#             value=st.session_state.form_inputs['atividade'],
#             placeholder="Digite a atividade"
#         )
#         evento = st.text_input(
#             "Evento", 
#             value=st.session_state.form_inputs['evento'],
#             placeholder="Digite o evento"
#         )
#         causa = st.text_input(
#             "Causa", 
#             value=st.session_state.form_inputs['causa'],
#             placeholder="Digite a causa"
#         )

#         submit_button = st.form_submit_button(label='Obter Oportunidade de melhorias')

#         if submit_button:
#             st.session_state.form_inputs = {
#                 'ramo_empresa': ramo_empresa,
#                 'nome_processo': nome_processo,
#                 'atividade': atividade,
#                 'evento': evento,
#                 'causa': causa
#             }

#             if ramo_empresa and st.session_state.oportunidades and nome_processo and atividade and evento and causa:
#                 start_time = time.time()
                
#                 # Inicializar ou redefinir `all_resultados` como DataFrame, se não existir
#                 if 'all_resultados' not in st.session_state or not isinstance(st.session_state.all_resultados, pd.DataFrame):
#                     st.session_state.all_resultados = pd.DataFrame(columns=['oportunidade'])  # Definir estrutura inicial

#                 # Criar uma lista para armazenar novos resultados desta execução
#                 new_resultados = []

#                 # Converter oportunidade para lista, caso seja uma string
#                 oportunidade = (
#                     [st.session_state.oportunidades] 
#                     if isinstance(st.session_state.oportunidades, str) 
#                     else st.session_state.oportunidades
#                 )

#                 total_oportunidade = len(oportunidade)

#                 for i, direcao in enumerate(oportunidade, start=1):

#                     # Verificar se o oportunidade já foi processado
#                     if direcao not in st.session_state.all_resultados['oportunidade'].values:
#                         # Criar o texto do processo
#                         processo = f"""ramo_empresa: {ramo_empresa}, oportunidade: {direcao}, nome_do_processo: {nome_processo}, atividade: {atividade}, evento: {evento}, causa: {causa}"""
                        
#                         # Definir a mensagem do spinner
#                         if len(oportunidade) == 1:
#                             mensagem_spinner = f"Seus dados estão sendo processados! Aguarde um instante (oportunidade {i}/{len(oportunidade)})"
#                         elif i == len(oportunidade):
#                             mensagem_spinner = f"Estamos quase lá! (oportunidade {i}/{len(oportunidade)})"
#                         else:
#                             mensagem_spinner = f"Seus dados estão sendo processados! Aguarde um instante (oportunidade {i}/{len(oportunidade)})"
                        
#                         # Spinner individual para o oportunidade
#                         with st.spinner(mensagem_spinner):
#                             analyst = run_agent_analysis(processo)
                        
#                         if isinstance(analyst, pd.DataFrame):  # Certificar que o retorno é DataFrame
#                             analyst['oportunidade'] = direcao  # Adicionar a coluna 'oportunidade'
#                             new_resultados.append(analyst)

#                 # Atualizar resultados com os novos oportunidade processados
#                 if new_resultados:
#                     # Concatenar novos resultados ao DataFrame existente na sessão
#                     new_resultados_df = pd.concat(new_resultados, ignore_index=True)
#                     resultado_final = pd.concat([st.session_state.all_resultados, new_resultados_df], ignore_index=True)
                    
#                     execution_time = time.time() - start_time
#                     st.success(f"Oportunidade de melhorias obtidas para {len(oportunidade)} oportunidade em {execution_time:.2f} segundos.")
                    
#                     # Preparar resultados para download
#                     st.session_state.resultados = resultado_final
#                     st.session_state.excel_file = convert_df_to_excel(resultado_final)
#                     st.session_state.show_download_button = True
#                 else:
#                     st.info("Nenhum novo oportunidade foi processado. Todos já foram analisados anteriormente.")
#             else:
#                 st.warning("Por favor, preencha todos os campos e adicione pelo menos um oportunidade.")

#     if hasattr(st.session_state, 'show_download_button') and st.session_state.show_download_button:
#         st.download_button(
#             label="📥Baixar Excel",
#             data=st.session_state.excel_file,
#             file_name='oportunidade_melhoria.xlsx',
#             mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
#         )
#         # st.rerun()
# def render_planilha_final():
#     if 'resultados' not in st.session_state:
#         st.warning("Não foi executado a obtenção das Oportunidade de melhorias.")
#         return
#     resultados = st.session_state.resultados
#     st.session_state.resultados_dict = resultados.to_dict('records')

#     st.write("## Planilha Final")
#     changes_made = False
#     deleted_indices = set()

#     for idx, row in enumerate(st.session_state.resultados_dict):
#         if idx in deleted_indices:  # Skip opportunities already marked for deletion
#             continue
        
#         with st.form(key=f'opportunity_form_{idx}'):
#             st.write(f"### Oportunidade {idx + 1} - oportunidade: {row.get('oportunidade', 'N/A')}")
            
#             oportunidade_de_melhoria = st.text_area(
#                 "Oportunidade de Melhoria", 
#                 value=row['Oportunidade de Melhoria'], 
#                 height=100
#             )
#             solucao = st.text_area(
#                 "Solução", 
#                 value=row['Solução'], 
#                 height=100
#             )
#             backlog_de_atividades = st.text_area(
#                 "Backlog de Atividades", 
#                 value=row.get('Backlog de Atividades', ''), 
#                 height=100
#             )
#             investimento = st.text_area(
#                 "Investimento", 
#                 value=row.get('Investimento', ''), 
#                 height=100
#             )
#             ganhos = st.text_area(
#                 "Ganhos", 
#                 value=row.get('Ganhos', ''), 
#                 height=100
#             )
            
#             col1, col2 = st.columns(2)
#             with col1:
#                 save_button = st.form_submit_button(label=f"Salvar Edição para Oportunidade {idx + 1}")
#             with col2:
#                 delete_button = st.form_submit_button(label=f"Excluir Oportunidade {idx + 1}", type="secondary")
            
#             if save_button:
#                 row.update({
#                     'Oportunidade de Melhoria': oportunidade_de_melhoria,
#                     'Solução': solucao,
#                     'Backlog de Atividades': backlog_de_atividades,
#                     'Investimento': investimento,
#                     'Ganhos': ganhos
#                 })
#                 changes_made = True
#                 st.success(f"Edição salva para Oportunidade {idx + 1}")
            
#             if delete_button:
#                 deleted_indices.add(idx)
#                 st.warning(f"Oportunidade {idx + 1} marcada para exclusão.")

#     if deleted_indices:
#         st.session_state.resultados_dict = [
#             row for idx, row in enumerate(st.session_state.resultados_dict) if idx not in deleted_indices
#         ]
#         changes_made = True

#     if changes_made:
#         edited_df = pd.DataFrame(st.session_state.resultados_dict)
#         st.session_state.resultados = edited_df
#         st.session_state.excel_file = convert_df_to_excel(edited_df)
#         st.session_state.show_download_button = True

#     if hasattr(st.session_state, 'show_download_button') and st.session_state.show_download_button:
#         st.download_button(
#             label="📥 Baixar Excel com Todas as Edições",
#             data=st.session_state.excel_file,
#             file_name='Oportunidade_de_melhorias_final.xlsx',
#             mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
#         )

# def main():
#     st.set_page_config(page_title="Oportunidade de Melhoria", layout="wide")
#     add_bg_from_local('background.png')
#     load_css('style.css')
    
#     pages = setup_navigation()
#     progress_value = (st.session_state.current_page + 1) / len(pages)
    
#     col1, col2 = st.columns([3, 1])
#     with col1:
#         st.markdown(f'<p class="big-font">{pages[st.session_state.current_page]}</p>', unsafe_allow_html=True)
#     with col2:
#         st.image('logo.png', width=200)
    
#     st.progress(progress_value)

#     main_container = st.container()
#     with main_container:
#         if pages[st.session_state.current_page] == "🔍 Oportunidade de melhorias":
#             render_diagnostico()  
#         elif pages[st.session_state.current_page] == "📋 Planilha Final":
#             render_planilha_final()

#     col1, col2, col3 = st.columns(3)
#     with col1:
#         if st.session_state.current_page > 0:
#             if st.button("Anterior", key="prev_button"):
#                 st.session_state.current_page -= 1
#                 st.rerun()
#     with col3:
#         if st.session_state.current_page < len(pages) - 1:
#             if st.button("Próximo", key="next_button"):
#                 st.session_state.current_page += 1
#                 st.rerun()
#         elif st.session_state.current_page == len(pages) - 1:
#             if st.button("Finalizar", key="finish_button"):
#                 st.success("Processo finalizado com sucesso!")

# if __name__ == "__main__":
#     main()

import streamlit as st
import base64
from pathlib import Path
import os
from dotenv import load_dotenv
from process import run_agent_analysis  
import pandas as pd
from io import BytesIO
import time
import streamlit as st

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

all_resultados=[]

if 'oportunidades' not in st.session_state:
    st.session_state.oportunidades = []

def stylable_container(key, css_styles):
    st.markdown(f"""
        <style>
        div[data-testid="stHorizontalBlock"] > div:nth-child({key}) {{
            {css_styles}
        }}
        </style>
    """, unsafe_allow_html=True)
    return st.container()

# Colocando imagem de fundo
def add_bg_from_local(image_file):
    with Path(image_file).open("rb") as file:
        encoded_string = base64.b64encode(file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/png;base64,{encoded_string});
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def load_css(css_file):
    with open(css_file, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Estilização de botões
def get_button_style(button_class):
    if button_class == "current":
        return "background-color: #01374C; color: white; font-weight: bold; font-size: 24px;"
    elif button_class == "previous":
        return "background-color: #4B4843; color: white; font-weight: normal; font-size: 24px;"
    else:
        return "background-color: #4B484340; color: #333333; font-size: 18px;"

# Sidebar e navegação entre páginas
def setup_navigation():
    st.sidebar.markdown("<h1 style='text-align: center; color: #AC8D61;'>Navegação</h1>", unsafe_allow_html=True)
    
    pages = ["🔍 Oportunidade de melhorias", "📋 Planilha Final"]
    
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 0

    for i, page in enumerate(pages):
        button_class = "current" if i == st.session_state.current_page else "previous" if i == st.session_state.current_page - 1 else ""

        if st.sidebar.button(page, key=f"nav_{i}", use_container_width=True, disabled=(i == st.session_state.current_page)):
            st.session_state.current_page = i
            st.rerun()

        st.markdown(f"""
            <style>
            div.row-widget.stButton > button[key="nav_{i}"] {{
                {get_button_style(button_class)}
            }}
            </style>
            """, unsafe_allow_html=True)

    return pages

# Adicionando oportunidade
def add_oportunidade(new_oportunidade):
    if new_oportunidade and new_oportunidade not in st.session_state.oportunidades:
        st.session_state.oportunidades.append(new_oportunidade)
        return True
    return False

# Removendo oportunidade
def remove_oportunidade(oportunidade_to_remove):
    if oportunidade_to_remove in st.session_state.oportunidades:
        st.session_state.oportunidades.remove(oportunidade_to_remove)

# Função para gerar excel
def convert_df_to_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Oportunidade de melhorias', index=False)
        for column in df:
            column_width = max(df[column].astype(str).map(len).max(), len(column))
            col_idx = df.columns.get_loc(column)
            writer.sheets['Oportunidade de melhorias'].column_dimensions[chr(65 + col_idx)].width = column_width + 2
    return output.getvalue()


def render_diagnostico():
    if 'form_inputs' not in st.session_state:
        st.session_state.form_inputs = {
            'ramo_empresa': '',
            'nome_processo': '',
            'atividade': '',
            'evento': '',
            'causa': ''
        }
    
    if 'all_resultados' not in st.session_state:
        st.session_state.all_resultados = []
        
    st.write("## Oportunidade de Melhoria")

    with st.form(key='add_oportunidade_form'):
        new_oportunidade = st.text_input(
            "Nova Oportunidade",
            placeholder="Digite uma oportunidade",
            key="new_oportunidade"
        )
        if st.form_submit_button("Adicionar Oportunidade"):
            if add_oportunidade(new_oportunidade):
                st.success(f"Oportunidade '{new_oportunidade}' adicionado com sucesso!")
                st.rerun()
            else:
                if not new_oportunidade:
                    st.warning("Por favor, digite uma oportunidade.")
                else:
                    st.warning("Esta oportunidade já existe.")

    for oportunidade in st.session_state.oportunidades:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.text(oportunidade)
        with col2:
            if st.button("Remover", key=f"remove_{oportunidade}"):
                remove_oportunidade(oportunidade)
                st.rerun()

    with st.form(key='oportunidade_melhoria_form'):
        ramo_empresa = st.text_input(
            "Ramo da empresa", 
            value=st.session_state.form_inputs['ramo_empresa'],
            placeholder="Digite o ramo da empresa"
        )
        nome_processo = st.text_input(
            "Nome do processo", 
            value=st.session_state.form_inputs['nome_processo'],
            placeholder="Digite o nome do processo"
        )
        atividade = st.text_input(
            "Atividade", 
            value=st.session_state.form_inputs['atividade'],
            placeholder="Digite a atividade"
        )
        evento = st.text_input(
            "Evento", 
            value=st.session_state.form_inputs['evento'],
            placeholder="Digite o evento"
        )
        causa = st.text_input(
            "Causa", 
            value=st.session_state.form_inputs['causa'],
            placeholder="Digite a causa"
        )

        submit_button = st.form_submit_button(label='Obter Oportunidade de melhorias')

        if submit_button:
            st.session_state.form_inputs = {
                'ramo_empresa': ramo_empresa,
                'nome_processo': nome_processo,
                'atividade': atividade,
                'evento': evento,
                'causa': causa
            }

            if ramo_empresa and st.session_state.oportunidades and nome_processo and atividade and evento and causa:
                start_time = time.time()
                
                # Inicializar ou redefinir `all_resultados` como DataFrame, se não existir
                if 'all_resultados' not in st.session_state or not isinstance(st.session_state.all_resultados, pd.DataFrame):
                    st.session_state.all_resultados = pd.DataFrame(columns=['oportunidade'])  # Definir estrutura inicial

                # Criar uma lista para armazenar novos resultados desta execução
                new_resultados = []

                # Converter oportunidade para lista, caso seja uma string
                oportunidade = (
                    [st.session_state.oportunidades] 
                    if isinstance(st.session_state.oportunidades, str) 
                    else st.session_state.oportunidades
                )

                total_oportunidade = len(oportunidade)

                for i, direcao in enumerate(oportunidade, start=1):

                    # Verificar se o oportunidade já foi processado
                    if direcao not in st.session_state.all_resultados['oportunidade'].values:
                        # Criar o texto do processo
                        processo = f"""ramo_empresa: {ramo_empresa}, oportunidade: {direcao}, nome_do_processo: {nome_processo}, atividade: {atividade}, evento: {evento}, causa: {causa}"""
                        
                        # Definir a mensagem do spinner
                        if len(oportunidade) == 1:
                            mensagem_spinner = f"Seus dados estão sendo processados! Aguarde um instante (oportunidade {i}/{len(oportunidade)})"
                        elif i == len(oportunidade):
                            mensagem_spinner = f"Estamos quase lá! (oportunidade {i}/{len(oportunidade)})"
                        else:
                            mensagem_spinner = f"Seus dados estão sendo processados! Aguarde um instante (oportunidade {i}/{len(oportunidade)})"
                        
                        # Spinner individual para o oportunidade
                        with st.spinner(mensagem_spinner):
                            analyst = run_agent_analysis(processo)
                        
                        if isinstance(analyst, pd.DataFrame):  # Certificar que o retorno é DataFrame
                            analyst['oportunidade'] = direcao  # Adicionar a coluna 'oportunidade'
                            new_resultados.append(analyst)

                # Atualizar resultados com os novos oportunidade processados
                if new_resultados:
                    # Concatenar novos resultados ao DataFrame existente na sessão
                    new_resultados_df = pd.concat(new_resultados, ignore_index=True)
                    resultado_final = pd.concat([st.session_state.all_resultados, new_resultados_df], ignore_index=True)
                    
                    execution_time = time.time() - start_time
                    st.success(f"Oportunidade de melhorias obtidas para {len(oportunidade)} oportunidade em {execution_time:.2f} segundos.")
                    
                    # Preparar resultados para download
                    st.session_state.resultados = resultado_final
                    st.session_state.excel_file = convert_df_to_excel(resultado_final)
                    st.session_state.show_download_button = True
                else:
                    st.info("Nenhum novo oportunidade foi processado. Todos já foram analisados anteriormente.")
            else:
                st.warning("Por favor, preencha todos os campos e adicione pelo menos um oportunidade.")

    if hasattr(st.session_state, 'show_download_button') and st.session_state.show_download_button:
        st.download_button(
            label="📥Baixar Excel",
            data=st.session_state.excel_file,
            file_name='oportunidade_melhoria.xlsx',
            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        # st.rerun()
def render_planilha_final():
    if 'resultados' not in st.session_state:
        st.warning("Não foi executado a obtenção das Oportunidade de melhorias.")
        return
    resultados = st.session_state.resultados
    st.session_state.resultados_dict = resultados.to_dict('records')

    st.write("## Planilha Final")
    changes_made = False
    deleted_indices = set()

    for idx, row in enumerate(st.session_state.resultados_dict):
        if idx in deleted_indices:  # Skip opportunities already marked for deletion
            continue
        
        with st.form(key=f'opportunity_form_{idx}'):
            st.write(f"### Oportunidade {idx + 1} - oportunidade: {row.get('oportunidade', 'N/A')}")
            
            oportunidade_de_melhoria = st.text_area(
                "Oportunidade de Melhoria", 
                value=row['Oportunidade de Melhoria'], 
                height=100
            )
            solucao = st.text_area(
                "Solução", 
                value=row['Solução'], 
                height=100
            )
            backlog_de_atividades = st.text_area(
                "Backlog de Atividades", 
                value=row.get('Backlog de Atividades', ''), 
                height=100
            )
            investimento = st.text_area(
                "Investimento", 
                value=row.get('Investimento', ''), 
                height=100
            )
            ganhos = st.text_area(
                "Ganhos", 
                value=row.get('Ganhos', ''), 
                height=100
            )
            
            col1, col2 = st.columns(2)
            with col1:
                save_button = st.form_submit_button(label=f"Salvar Edição para Oportunidade {idx + 1}")
            with col2:
                delete_button = st.form_submit_button(label=f"Excluir Oportunidade {idx + 1}", type="secondary")
            
            if save_button:
                row.update({
                    'Oportunidade de Melhoria': oportunidade_de_melhoria,
                    'Solução': solucao,
                    'Backlog de Atividades': backlog_de_atividades,
                    'Investimento': investimento,
                    'Ganhos': ganhos
                })
                changes_made = True
                st.success(f"Edição salva para Oportunidade {idx + 1}")
            
            if delete_button:
                deleted_indices.add(idx)
                st.warning(f"Oportunidade {idx + 1} marcada para exclusão.")

    if deleted_indices:
        st.session_state.resultados_dict = [
            row for idx, row in enumerate(st.session_state.resultados_dict) if idx not in deleted_indices
        ]
        changes_made = True

    if changes_made:
        edited_df = pd.DataFrame(st.session_state.resultados_dict)
        st.session_state.resultados = edited_df
        st.session_state.excel_file = convert_df_to_excel(edited_df)
        st.session_state.show_download_button = True

    if hasattr(st.session_state, 'show_download_button') and st.session_state.show_download_button:
        st.download_button(
            label="📥 Baixar Excel com Todas as Edições",
            data=st.session_state.excel_file,
            file_name='Oportunidade_de_melhorias_final.xlsx',
            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )

def main():
    st.set_page_config(page_title="Oportunidade de Melhoria", layout="wide")
    add_bg_from_local('background.png')
    load_css('style.css')
    
    pages = setup_navigation()
    progress_value = (st.session_state.current_page + 1) / len(pages)
    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown(f'<p class="big-font">{pages[st.session_state.current_page]}</p>', unsafe_allow_html=True)
    with col2:
        st.image('logo.png', width=200)
    
    st.progress(progress_value)

    main_container = st.container()
    with main_container:
        if pages[st.session_state.current_page] == "🔍 Oportunidade de melhorias":
            render_diagnostico()  
        elif pages[st.session_state.current_page] == "📋 Planilha Final":
            render_planilha_final()

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.session_state.current_page > 0:
            if st.button("Anterior", key="prev_button"):
                st.session_state.current_page -= 1
                st.rerun()
    with col3:
        if st.session_state.current_page < len(pages) - 1:
            if st.button("Próximo", key="next_button"):
                st.session_state.current_page += 1
                st.rerun()
        elif st.session_state.current_page == len(pages) - 1:
            if st.button("Finalizar", key="finish_button"):
                st.success("Processo finalizado com sucesso!")

if __name__ == "__main__":
    main()