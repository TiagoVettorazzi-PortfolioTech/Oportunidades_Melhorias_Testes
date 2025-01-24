import os
import sys
from dotenv import load_dotenv
import dspy
from openai import OpenAI
import weaviate
from dspy.retrieve.weaviate_rm import WeaviateRM
import streamlit as st
 
# Carrega o .env para configurar a chave OPENAI_API_KEY
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
 
# Verifica se a chave foi carregada corretamente
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables.")
 
# Configura o diretório atual
os.chdir(os.path.abspath(os.curdir))
 
def custom_excepthook(exctype, value, traceback):
    print(f"Exception type: {exctype}")
    print(f"Exception value: {value}")
    print("Traceback details:")
    return sys.__excepthook__(exctype, value, traceback)
 
sys.excepthook = custom_excepthook
 
try:
    class Oportune_op(dspy.Signature):
        """
            ** Contexto: **
            Você é um experiente Gerente de Projetos e Processos de uma grande empresa.
            Sua tarefa é detalhar uma única oportunidade de melhoria fornecida pelo cliente, descrevendo solução,
            backlog, investimentos necessários e ganhos esperados.
 
            ** EXEMPLO DE ENTRADA DE DADOS: **
                - oportunidade_melhoria: texto da oportunidade fornecida pelo cliente.
            """  
 
            # # OPORTUNIDADE DE MELHORIA FORNECIDA PELO USUÁRIO
            # oportunidade_melhoria = dspy.InputField(desc="Descreva a oportunidade de melhoria a ser detalhada.")
 
            # RESPOSTA DETALHADA
        answer = dspy.OutputField(desc="""Para a oportunidade de melhoria fornecida, detalhe os seguintes campos:
                                        **Oportunidade de Melhoria** : Automatização de Captura de Informações de Pagamentos:
                                     
                                        **Solução** : Desenvolver uma integração com o sistema bancário para captura automática de informações sobre pagamentos realizados e recusados. Isso inclui a baixa automática dos pagamentos no sistema e notificações para as áreas interessadas em caso de problemas.
                                       
                                        **Backlog de Atividades:** Sugestões de atividades específicas que podem ser adicionadas a um backlog de implementação para atingir a solução.
                                       
                                        **Investimento** : Horas para desenvolvimento de customizações e implantação do projeto.
                                       
                                        **Ganhos:** Automação de atividades manuais e repetitivas, maior agilidade no processo, redução do
                                        risco de erros operacionais e simplificação da disseminação de informações entre as partes interessadas.
 
                                        Dê sugestões simples e eficientes de acordo com o seu conhecimento e contexto.
                                        Pense passo a passo, gerando mais de uma resposta, avalie cada passo e veja qual dos sugeridos
                                        é o mais adequado.
                                        RESPONDA em Português do Brasil.
                                """)
           
        # TEXTO DO PROBLEMA DE ENTRADA
        question = dspy.InputField()
        # AQUI TEMOS AS OPORTUNIDADES QUE VEM DA BASE FRIA (NO CASO ESTAMOS USANDO 5 PASSAGES)
        context = dspy.InputField(desc="Com base na Oportunidade de Melhoria identificada, desenvolva-a")    
   
    class OportuneRAG_op(dspy.Module):
        def __init__(self, num_passages=5):
            super().__init__()
       
            self.retrieve = dspy.Retrieve(k=num_passages)
            self.generate_answer = dspy.ChainOfThought(Oportune_op) # Step by Step Cadeia de pensamento...
 
        def forward(self, question):
            context = self.retrieve(question).passages
            prediction = self.generate_answer(context=context, question=question)        
            return dspy.Prediction(context=context, answer=prediction.answer)  
 
except Exception as e:
    print(f"ERRO CLASSES: {e}")
 
print('dspy_DocsOportune.py: OK')














