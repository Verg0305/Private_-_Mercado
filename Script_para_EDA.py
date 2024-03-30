import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn as sk
import seaborn as sns
import streamlit as st
import openai

# Baixando as Bases

## Baixando as Bases de Fundos do Private
caminho_fundos_private = "C:/Users/rodri/OneDrive/Área de Trabalho/Deep Learning/Projeto com Streamlit/Base de Dados/Dados Fundos Private.xlsx"
Totalizadores_Dados_Fundos_Private = pd.read_excel(caminho_fundos_private, sheet_name='Private_Totalizadores')
Fundos_Proprios_Dados_Fundos_Private = pd.read_excel(caminho_fundos_private, sheet_name='Private_Fundos_Próprios')
Fundos_Terceiros_Dados_Fundos_Private = pd.read_excel(caminho_fundos_private, sheet_name='Private_Fundos_Terceiros')
Fundos_Exclusivos_Dados_Fundos_Private = pd.read_excel(caminho_fundos_private, sheet_name='Private_Fundos_Exclusivos')
Fundos_Estruturados_Dados_Fundos_Private = pd.read_excel(caminho_fundos_private, sheet_name='Private_Fundos_Estruturados')

## Baixando as Bases de Dados Geeográficos
caminho_dados_geograficos_private = "C:/Users/rodri/OneDrive/Área de Trabalho/Deep Learning/Projeto com Streamlit/Base de Dados/Dados Geográficos Private.xlsx"
Volume_Financeiro_por_regiao_Dados_Geograficos_Private = pd.read_excel(caminho_dados_geograficos_private, sheet_name='Private_Vol_Financeiro_Região')
Grupos_Economicos_por_regiao_Dados_Geograficos_Private = pd.read_excel(caminho_dados_geograficos_private, sheet_name='Private_Grupos_Econ_Região')
Contas_por_regiao_Dados_Geograficos_Private = pd.read_excel(caminho_dados_geograficos_private, sheet_name='Private_Contas_Região')

## Baixando as Bases de Fundos do Mercado
caminho_fundos_mercado = "C:/Users/rodri/OneDrive/Área de Trabalho/Deep Learning/Projeto com Streamlit/Base de Dados/Dados Indústria Fundos Brasil.xlsx"
PL_Total_Dados_Mercado_Fundos = pd.read_excel(caminho_fundos_mercado, sheet_name='Mercado_PL_Total')
PL_Por_Classe_Dados_Mercado_Fundos = pd.read_excel(caminho_fundos_mercado, sheet_name='Mercado_PL_Por_Classe')

## Baixando Base de Dados Dólar
Historico_Dolar = pd.read_excel("C:/Users/rodri/OneDrive/Área de Trabalho/Deep Learning/Projeto com Streamlit/Base de Dados/Histórico Dólar.xlsx")

## Baixando Base de Dados Ibovespa
Historico_Ibovespa = pd.read_excel("C:/Users/rodri/OneDrive/Área de Trabalho/Deep Learning/Projeto com Streamlit/Base de Dados/Histórico Ibovespa.xlsx")

## Baixando Base de Dados Selic
Historico_Selic = pd.read_excel("C:/Users/rodri/OneDrive/Área de Trabalho/Deep Learning/Projeto com Streamlit/Base de Dados/Histórico Selic.xlsx")


                                       
# Começando a trabalhar no Streamlit
st.title("Private Banking & Mercado Agregado: Análise Comparativa do Patrimônio Líquido de Fundos de Investimento")
st.subheader("Esta aplicação permite visualizar a evolução do Patrimônio Líquido (PL) de fundos de investimento do Segmento de Private Banking e do Mercado Agregado do Brasil.")

# Modificar os nomes das colunas para remoção dos underscores
Totalizadores_Dados_Fundos_Private.columns = Totalizadores_Dados_Fundos_Private.columns.str.replace('_', ' ')
PL_Por_Classe_Dados_Mercado_Fundos.columns = PL_Por_Classe_Dados_Mercado_Fundos.columns.str.replace('_', ' ')

# Definir as opções para as colunas do eixo y para cada conjunto de dados
opcoes_colunas_private = Totalizadores_Dados_Fundos_Private.columns.drop("Data").tolist()
opcoes_colunas_mercado = PL_Por_Classe_Dados_Mercado_Fundos.columns.drop("Data").tolist()

# Seleção das colunas para os Fundos Private
colunas_selecionadas_private = st.multiselect("Selecione as Classes (Private Banking)", opcoes_colunas_private)


# Seleção das colunas para os Fundos de Mercado
colunas_selecionadas_mercado = st.multiselect("Selecione as Classes (Mercado Agregado)", opcoes_colunas_mercado)

# Verificar se alguma coluna foi selecionada em pelo menos um dos conjuntos de dados
if colunas_selecionadas_private or colunas_selecionadas_mercado:
    # Gerar o gráfico de linha com os dados selecionados
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plotar os dados dos fundos private
    for coluna in colunas_selecionadas_private:
        sns.lineplot(data=Totalizadores_Dados_Fundos_Private, x='Data', y=coluna, label=f"Private - {coluna}", ax=ax)

    # Plotar os dados dos fundos de mercado
    for coluna in colunas_selecionadas_mercado:
        sns.lineplot(data=PL_Por_Classe_Dados_Mercado_Fundos, x='Data', y=coluna, label=f"Mercado - {coluna}", ax=ax)

    ax.set_title('Comparação de Dados de Fundos de Investimento', fontsize=16, pad=20, fontweight='bold')
    ax.set_xlabel('Data', fontsize=12)
    ax.set_ylabel('Valores', fontsize=12)
    ax.legend(loc='upper left', fontsize=10).set_bbox_to_anchor((0.05, 0.95))
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.tick_params(axis='both', labelsize=10)
    ax.xaxis.label.set_rotation(45)
    ax.xaxis.set_tick_params(rotation=45)
    ax.yaxis.labelpad = 20
    ax.xaxis.labelpad = 20
    ax.legend(loc='upper left', fontsize=10).set_bbox_to_anchor((0.05, 0.95))
    ax.set_facecolor('whitesmoke')
    plt.tight_layout()
    st.pyplot(fig)
else:
    st.warning("Por favor, selecione pelo menos uma classe de Fundos para visualização.")
    
#####################################################################################################

# Extraindo as colunas disponíveis para seleção, excluindo a coluna "Data"
opcoes_colunas_private = Totalizadores_Dados_Fundos_Private.columns.drop("Data").tolist()
opcoes_colunas_mercado = PL_Por_Classe_Dados_Mercado_Fundos.columns.drop("Data").tolist()
opcoes_colunas_dolar = Historico_Dolar.columns.drop("Data").tolist()
opcoes_colunas_ibovespa = Historico_Ibovespa.columns.drop("Data").tolist()
opcoes_colunas_selic = Historico_Selic.columns.drop("Data").tolist()

# Criando a aplicação Streamlit
st.subheader("Esta aplicação permite visualizar a matriz de correlação entre as variáveis selecionadas.")

# Seleção das variáveis para a matriz de correlação
colunas_selecionadas_private = st.multiselect('Selecione as variáveis (Private Banking)', opcoes_colunas_private)
colunas_selecionadas_mercado = st.multiselect('Selecione as variáveis (Mercado Agregado)', opcoes_colunas_mercado)

# Opções para Dólar, Ibovespa e Selic agrupadas em um único multiselect
opcoes_colunas_dolar_ibovespa_selic = opcoes_colunas_dolar + opcoes_colunas_ibovespa + opcoes_colunas_selic
colunas_selecionadas_dolar_ibovespa_selic = st.multiselect('Selecione entre as variáveis de Dólar, Ibovespa e Selic', opcoes_colunas_dolar_ibovespa_selic)

# Concatenando as variáveis selecionadas de todas as fontes de dados
colunas_selecionadas = (colunas_selecionadas_private + colunas_selecionadas_mercado + 
                        colunas_selecionadas_dolar_ibovespa_selic)

# Removendo duplicatas e mantendo a ordem da seleção
colunas_selecionadas = list(dict.fromkeys(colunas_selecionadas))

# Verificando se há variáveis selecionadas
if colunas_selecionadas:
    # Filtrando as variáveis selecionadas de cada tabela
    dados_private = Totalizadores_Dados_Fundos_Private[colunas_selecionadas_private] if colunas_selecionadas_private else pd.DataFrame()
    dados_mercado = PL_Por_Classe_Dados_Mercado_Fundos[colunas_selecionadas_mercado] if colunas_selecionadas_mercado else pd.DataFrame()
    
    dados_dolar = Historico_Dolar[colunas_selecionadas_dolar_ibovespa_selic] if 'Dólar' in colunas_selecionadas_dolar_ibovespa_selic else pd.DataFrame()
    dados_ibovespa = Historico_Ibovespa[colunas_selecionadas_dolar_ibovespa_selic] if 'Ibovespa' in colunas_selecionadas_dolar_ibovespa_selic else pd.DataFrame()
    dados_selic = Historico_Selic[colunas_selecionadas_dolar_ibovespa_selic] if 'Selic' in colunas_selecionadas_dolar_ibovespa_selic else pd.DataFrame()

    # Concatenando os dados de todas as fontes
    dados = pd.concat([dados_private, dados_mercado, dados_dolar, dados_ibovespa, dados_selic], axis=1)

    # Calculando a matriz de correlação
    matriz_correlacao = dados.corr()

    # Traçando a matriz de correlação usando seaborn
    plt.figure(figsize=(10, 8))
    sns.heatmap(matriz_correlacao, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
    plt.title('Matriz de Correlação entre Variáveis Selecionadas')
    plt.xticks(rotation=45)
    plt.yticks(rotation=45)
    fig, ax = plt.subplots()  # Criando a figura e o eixo
    ax = sns.heatmap(matriz_correlacao, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
    st.pyplot(fig)
else:
    st.warning('Selecione pelo menos uma variável.')
    
#################################################################################################################################

# Extraindo as colunas disponíveis para seleção, excluindo a coluna "Data"
opcoes_colunas_private = Totalizadores_Dados_Fundos_Private.columns.drop("Data").tolist()
opcoes_colunas_mercado = PL_Por_Classe_Dados_Mercado_Fundos.columns.drop("Data").tolist()
opcoes_colunas_dolar = Historico_Dolar.columns.drop("Data").tolist()
opcoes_colunas_ibovespa = Historico_Ibovespa.columns.drop("Data").tolist()
opcoes_colunas_selic = Historico_Selic.columns.drop("Data").tolist()

# Criando a aplicação Streamlit
st.subheader("Elasticidade entre Variáveis")

# Seleção das variáveis para a elasticidade
var_x = st.selectbox('Selecione a primeira variável', opcoes_colunas_private + opcoes_colunas_mercado + opcoes_colunas_dolar + opcoes_colunas_ibovespa + opcoes_colunas_selic)
var_y = st.selectbox('Selecione a segunda variável', opcoes_colunas_private + opcoes_colunas_mercado + opcoes_colunas_dolar + opcoes_colunas_ibovespa + opcoes_colunas_selic)

# Verificar se duas variáveis foram selecionadas
if var_x and var_y:
    # Função para calcular a elasticidade entre duas colunas
    def calcular_elasticidade(coluna_x, coluna_y):
        percent_change_x = (coluna_x.iloc[-1] - coluna_x.iloc[0]) / coluna_x.iloc[0] * 100
        percent_change_y = (coluna_y.iloc[-1] - coluna_y.iloc[0]) / coluna_y.iloc[0] * 100
        elasticidade = percent_change_y / percent_change_x
        return elasticidade

    # Determinar de qual tabela cada variável vem
    if var_x in opcoes_colunas_private:
        tabela_var_x = Totalizadores_Dados_Fundos_Private
    elif var_x in opcoes_colunas_mercado:
        tabela_var_x = PL_Por_Classe_Dados_Mercado_Fundos
    elif var_x in opcoes_colunas_dolar:
        tabela_var_x = Historico_Dolar
    elif var_x in opcoes_colunas_ibovespa:
        tabela_var_x = Historico_Ibovespa
    elif var_x in opcoes_colunas_selic:
        tabela_var_x = Historico_Selic

    if var_y in opcoes_colunas_private:
        tabela_var_y = Totalizadores_Dados_Fundos_Private
    elif var_y in opcoes_colunas_mercado:
        tabela_var_y = PL_Por_Classe_Dados_Mercado_Fundos
    elif var_y in opcoes_colunas_dolar:
        tabela_var_y = Historico_Dolar
    elif var_y in opcoes_colunas_ibovespa:
        tabela_var_y = Historico_Ibovespa
    elif var_y in opcoes_colunas_selic:
        tabela_var_y = Historico_Selic

    # Calcular a elasticidade entre as duas variáveis
    elasticidade = calcular_elasticidade(tabela_var_x[var_x], tabela_var_y[var_y])
    st.write(f'Elasticidade entre {var_x} e {var_y}: {elasticidade:.2f}')
else:
    st.warning('Selecione duas variáveis.')