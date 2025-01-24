from modeloDSpy_op import OportuneRAGClient
from transform_input_to_df_op import transform_input_to_df_op

def run_agent_analysis_op(prompt):
    """
    Executa a análise utilizando os agentes OportuneRAGClient e transform_input_to_df.
    
    Parâmetros:
    prompt (str): Prompt a ser enviado para o agente OportuneRAGClient.
    
    Retorna:
    pandas.DataFrame: Resultado da análise.
    """
    client = OportuneRAGClient()
    answer = client.run_model(prompt)
    df = transform_input_to_df_op(answer)
    # client.close_weaviate_client()
    return df
# print(run_agent_analysis_op("Teste para criar oportunidade de melhoria"))