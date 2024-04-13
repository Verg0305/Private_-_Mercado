import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn as sk
import seaborn as sns
import streamlit as st


# Baixando as Bases

## Baixando as Bases de Fundos do Private
caminho_fundos_private = "Base de Dados/Dados Fundos Private.xlsx"
Totalizadores_Dados_Fundos_Private = pd.read_excel(caminho_fundos_private, sheet_name='Private_Totalizadores')
Fundos_Proprios_Dados_Fundos_Private = pd.read_excel(caminho_fundos_private, sheet_name='Private_Fundos_Próprios')
Fundos_Terceiros_Dados_Fundos_Private = pd.read_excel(caminho_fundos_private, sheet_name='Private_Fundos_Terceiros')
Fundos_Exclusivos_Dados_Fundos_Private = pd.read_excel(caminho_fundos_private, sheet_name='Private_Fundos_Exclusivos')
Fundos_Estruturados_Dados_Fundos_Private = pd.read_excel(caminho_fundos_private, sheet_name='Private_Fundos_Estruturados')

## Baixando as Bases de Dados Geográficos
caminho_dados_geograficos_private = "Base de Dados/Dados Geográficos Private.xlsx"
Volume_Financeiro_por_regiao_Dados_Geograficos_Private = pd.read_excel(caminho_dados_geograficos_private, sheet_name='Private_Vol_Financeiro_Região')
Grupos_Economicos_por_regiao_Dados_Geograficos_Private = pd.read_excel(caminho_dados_geograficos_private, sheet_name='Private_Grupos_Econ_Região')
Contas_por_regiao_Dados_Geograficos_Private = pd.read_excel(caminho_dados_geograficos_private, sheet_name='Private_Contas_Região')

## Baixando as Bases de Fundos do Mercado
caminho_fundos_mercado = "Base de Dados/Dados Indústria Fundos Brasil.xlsx"
PL_Total_Dados_Mercado_Fundos = pd.read_excel(caminho_fundos_mercado, sheet_name='Mercado_PL_Total')
PL_Por_Classe_Dados_Mercado_Fundos = pd.read_excel(caminho_fundos_mercado, sheet_name='Mercado_PL_Por_Classe')

## Baixando Base de Dados Dólar
Historico_Dolar = pd.read_excel("Base de Dados/Histórico Dólar.xlsx")

## Baixando Base de Dados Ibovespa
Historico_Ibovespa = pd.read_excel("Base de Dados/Histórico Ibovespa.xlsx")

## Baixando Base de Dados Selic
Historico_Selic = pd.read_excel("Base de Dados/Histórico Selic.xlsx")


# Manipulação dos Dados:

# Colocando as Colunas em ordem Crescente

Totalizadores_Dados_Fundos_Private = Totalizadores_Dados_Fundos_Private[::-1].reset_index(drop=True)
Fundos_Proprios_Dados_Fundos_Private = Fundos_Proprios_Dados_Fundos_Private[::-1].reset_index(drop=True)
Fundos_Terceiros_Dados_Fundos_Private = Fundos_Terceiros_Dados_Fundos_Private[::-1].reset_index(drop=True)
Fundos_Exclusivos_Dados_Fundos_Private = Fundos_Exclusivos_Dados_Fundos_Private[::-1].reset_index(drop=True)
Fundos_Estruturados_Dados_Fundos_Private = Fundos_Estruturados_Dados_Fundos_Private[::-1].reset_index(drop=True)
Volume_Financeiro_por_regiao_Dados_Geograficos_Private = Volume_Financeiro_por_regiao_Dados_Geograficos_Private[::-1].reset_index(drop=True)
Grupos_Economicos_por_regiao_Dados_Geograficos_Private = Grupos_Economicos_por_regiao_Dados_Geograficos_Private[::-1].reset_index(drop=True)
Contas_por_regiao_Dados_Geograficos_Private = Contas_por_regiao_Dados_Geograficos_Private[::-1].reset_index(drop=True)
PL_Total_Dados_Mercado_Fundos = PL_Total_Dados_Mercado_Fundos[::-1].reset_index(drop=True)
PL_Por_Classe_Dados_Mercado_Fundos = PL_Por_Classe_Dados_Mercado_Fundos[::-1].reset_index(drop=True)
Historico_Dolar = Historico_Dolar[::-1].reset_index(drop=True)
Historico_Ibovespa = Historico_Ibovespa[::-1].reset_index(drop=True)
Historico_Selic = Historico_Selic[::-1].reset_index(drop=True)



# Criando evolução percentual acumulada

##Private_Totalizadores

# Lista de colunas e DataFrame para calcular a evolução percentual acumulada
colunas_para_calcular_Private_Totalizadores = [
    ('Var%_Volume_Financeiro_Total_Private', Totalizadores_Dados_Fundos_Private),
    ('Var%_PL_Total_Fundos_Private', Totalizadores_Dados_Fundos_Private),
    ('Var%_PL_Total_Renda_Fixa_Private', Totalizadores_Dados_Fundos_Private),
    ('Var%_PL_Total_Renda_Fixa_Duração_Baixa_Private', Totalizadores_Dados_Fundos_Private),
    ('Var%_PL_Total_Renda_Fixa_Outros_Private', Totalizadores_Dados_Fundos_Private),
    ('Var%_PL_Total_Multimercados_Private', Totalizadores_Dados_Fundos_Private),
    ('Var%_PL_Total_Ações_Private', Totalizadores_Dados_Fundos_Private),
    ('Var%_PL_Total_Cambial_Private', Totalizadores_Dados_Fundos_Private)
]

# Calcular a evolução percentual acumulada para cada coluna em cada DataFrame
for coluna, dataframe in colunas_para_calcular_Private_Totalizadores:
    dataframe[f'Evolução_Percentual_Acumulada_{coluna}'] = dataframe[coluna].cumsum()


##Private_Fundos_Próprios

# Lista de colunas e DataFrame para calcular a evolução percentual acumulada
colunas_para_calcular_Private_Fundos_Próprios = [
    ('Var%_Renda_Fixa_Duração_Baixa_Fundos_Proprios_Private', Fundos_Proprios_Dados_Fundos_Private),
    ('Var%_Renda_Fixa_Outros_Fundos_Proprios_Private', Fundos_Proprios_Dados_Fundos_Private),
    ('Var%_Multimercados_Fundos_Proprios_Private', Fundos_Proprios_Dados_Fundos_Private),
    ('Var%_Ações_Fundos_Proprios_Private', Fundos_Proprios_Dados_Fundos_Private),
    ('Var%_Cambial_Fundos_Proprios_Private', Fundos_Proprios_Dados_Fundos_Private)
]

# Calcular a evolução percentual acumulada para cada coluna em cada DataFrame
for coluna, dataframe in colunas_para_calcular_Private_Fundos_Próprios:
    Totalizadores_Dados_Fundos_Private[f'Evolução_Percentual_Acumulada_{coluna}'] = dataframe[coluna].cumsum()

##Private_Fundos_Terceiros

# Lista de colunas e DataFrame para calcular a evolução percentual acumulada
colunas_para_calcular_Private_Fundos_Terceiros = [
    ('Var%_Renda_Fixa_Duração_Baixa_Fundos_Terceiros_Private', Fundos_Terceiros_Dados_Fundos_Private),
    ('Var%_Renda_Fixa_Outros_Fundos_Terceiros_Private', Fundos_Terceiros_Dados_Fundos_Private),
    ('Var%_Multimercados_Fundos_Terceiros_Private', Fundos_Terceiros_Dados_Fundos_Private),
    ('Var%_Ações_Fundos_Terceiros_Private', Fundos_Terceiros_Dados_Fundos_Private),
    ('Var%_Cambial_Fundos_Terceiros_Private', Fundos_Terceiros_Dados_Fundos_Private)
]

# Calcular a evolução percentual acumulada para cada coluna em cada DataFrame
for coluna, dataframe in colunas_para_calcular_Private_Fundos_Terceiros:
    dataframe[f'Evolução_Percentual_Acumulada_{coluna}'] = dataframe[coluna].cumsum()


##Private_Fundos_Exclusivos

# Lista de colunas e DataFrame para calcular a evolução percentual acumulada
colunas_para_calcular_Private_Fundos_Exclusivos = [
    ('Var%_Renda_Fixa_Duração_Baixa_Fundos_Exclusivos_Private', Fundos_Exclusivos_Dados_Fundos_Private),
    ('Var%_Renda_Fixa_Outros_Fundos_Exclusivos_Private', Fundos_Exclusivos_Dados_Fundos_Private),
    ('Var%_Multimercados_Fundos_Exclusivos_Private', Fundos_Exclusivos_Dados_Fundos_Private),
    ('Var%_Ações_Fundos_Exclusivos_Private', Fundos_Exclusivos_Dados_Fundos_Private)
]

# Calcular a evolução percentual acumulada para cada coluna em cada DataFrame
for coluna, dataframe in colunas_para_calcular_Private_Fundos_Exclusivos:
    dataframe[f'Evolução_Percentual_Acumulada_{coluna}'] = dataframe[coluna].cumsum()


##Private_Fundos_Estruturados

# Lista de colunas e DataFrame para calcular a evolução percentual acumulada
colunas_para_calcular_Private_Fundos_Estruturados = [
    ('Var%_FIP_Fundos_Estruturados_Private', Fundos_Estruturados_Dados_Fundos_Private),
    ('Var%_FIDC_Fundos_Estruturados_Private', Fundos_Estruturados_Dados_Fundos_Private),
    ('Var%_FII_Fundos_Estruturados_Private', Fundos_Estruturados_Dados_Fundos_Private),
    ('Var%_Outros_Fundos_Estruturados_Private', Fundos_Estruturados_Dados_Fundos_Private)
]

# Calcular a evolução percentual acumulada para cada coluna em cada DataFrame
for coluna, dataframe in colunas_para_calcular_Private_Fundos_Estruturados:
    dataframe[f'Evolução_Percentual_Acumulada_{coluna}'] = dataframe[coluna].cumsum()

##Mercado_PL_Total

# Lista de colunas e DataFrame para calcular a evolução percentual acumulada
colunas_para_calcular_Mercado_PL_Total = [
    ('Var%_Mercado_PL_Total', PL_Total_Dados_Mercado_Fundos),
    ('Var%_Mercado_PL_ex_Previdência', PL_Total_Dados_Mercado_Fundos)
]

# Calcular a evolução percentual acumulada para cada coluna em cada DataFrame
for coluna, dataframe in colunas_para_calcular_Mercado_PL_Total:
    dataframe[f'Evolução_Percentual_Acumulada_{coluna}'] = dataframe[coluna].cumsum()


##Mercado_PL_Por_Classe

# Lista de colunas e DataFrame para calcular a evolução percentual acumulada
colunas_para_calcular_Mercado_PL_Por_Classe = [
    ('Var%_Mercado_PL_Renda_Fixa', PL_Por_Classe_Dados_Mercado_Fundos),
    ('Var%_Mercado_PL_Ações', PL_Por_Classe_Dados_Mercado_Fundos),
    ('Var%_Mercado_PL_Multimercado', PL_Por_Classe_Dados_Mercado_Fundos),
    ('Var%_Mercado_PL_Cambial', PL_Por_Classe_Dados_Mercado_Fundos),
    ('Var%_Mercado_PL_Previdência', PL_Por_Classe_Dados_Mercado_Fundos),
    ('Var%_Mercado_PL_ETF', PL_Por_Classe_Dados_Mercado_Fundos),
    ('Var%_Mercado_PL_FIDC', PL_Por_Classe_Dados_Mercado_Fundos),
    ('Var%_Mercado_PL_FIP', PL_Por_Classe_Dados_Mercado_Fundos),
    ('Var%_Mercado_PL_FII', PL_Por_Classe_Dados_Mercado_Fundos),
    ('Var%_Mercado_PL_Off_shore', PL_Por_Classe_Dados_Mercado_Fundos),
    ('Var%_Total', PL_Por_Classe_Dados_Mercado_Fundos)
]

# Calcular a evolução percentual acumulada para cada coluna em cada DataFrame
for coluna, dataframe in colunas_para_calcular_Mercado_PL_Por_Classe:
    dataframe[f'Evolução_Percentual_Acumulada_{coluna}'] = dataframe[coluna].cumsum()

##Historico_Dolar

# Calcular a evolução percentual acumulada para a coluna em cada DataFrame
coluna_Var_Dolar = 'Var%_Dólar'
Historico_Dolar[f'Evolução_Percentual_Acumulada_{coluna_Var_Dolar}'] = Historico_Dolar[coluna_Var_Dolar].cumsum()

##Historico_Ibovespa

# Calcular a evolução percentual acumulada para a coluna em cada DataFrame
coluna_Var_Ibovespa = 'Var%_Ibovespa'
Historico_Ibovespa[f'Evolução_Percentual_Acumulada_{coluna_Var_Ibovespa}'] = Historico_Ibovespa[coluna_Var_Ibovespa].cumsum()

##Historico_Selic

# Calcular a evolução percentual acumulada para a coluna em cada DataFrame
coluna_Var_Selic = 'Var%_Selic'
Historico_Selic[f'Evolução_Percentual_Acumulada_{coluna_Var_Selic}'] = Historico_Selic[coluna_Var_Selic].cumsum()



##########################################################################################################################################################################

# Começando a trabalhar no Streamlit
st.title("Private Banking & Mercado Agregado: Análise Comparativa da Evolução do Patrimônio Líquido de Fundos de Investimento")
st.subheader("Esta aplicação permite visualizar a tagetória da evolução do Patrimônio Líquido (PL) de fundos de investimento vinculados ao Segmento de Private Banking e o Mercado Agregado de fundos do Brasil.")
st.write("""
Minha dissertação versará sobre a diferença na formação / realocação de portfólio de investimentos entre clientes do segmento de Private Banking quando comparados ao agregado de investidores do mercado.
""")

st.write("""
O universo usado para estudo será o mercado de fundos de investimento brasileiro.
""")

st.write("""
Esta aplicação será de grande utilidade na visualização dinâmica das diferenças no comportamento das variáveis ao longo do tempo, tanto isoladamente quanto comparadas com o benchmark de referência.
""")

st.write("""
A matriz de correlação também fornecerá insights valiosos a respeito da diferença de comportamento entre os clientes do Segmento de Private Banking e o mercado agregado.
""")

# Carregar a imagem
imagem_path = "C:/Users/rodri/OneDrive/Área de Trabalho/Deep Learning/Projeto com Streamlit/Imagem3.jpg"

# Adicionar texto acima da imagem
st.sidebar.markdown("**Selecione as variáveis para análise:**")

# Exibir a imagem na barra lateral
st.sidebar.image(imagem_path, use_column_width=True, output_format='auto')

# Dicionário de mapeamento de nomes completos para nomes resumidos
mapeamento_colunas_resumidas = {
    'Evolução_Percentual_Acumulada_Var%_Volume_Financeiro_Total_Private': 'Private - Var% Vol Financeiro Total ',
    'Evolução_Percentual_Acumulada_Var%_PL_Total_Fundos_Private': 'Private - Var% PL Total Fundos',
    'Evolução_Percentual_Acumulada_Var%_PL_Total_Renda_Fixa_Private': 'Private - Var% PL Renda Fixa',
    'Evolução_Percentual_Acumulada_Var%_PL_Total_Renda_Fixa_Duração_Baixa_Private': 'Private - Var% PL Renda Fixa Duração Baixa',
    'Evolução_Percentual_Acumulada_Var%_PL_Total_Renda_Fixa_Outros_Private': 'Private - Var% PL Renda Fixa',
    'Evolução_Percentual_Acumulada_Var%_PL_Total_Multimercados_Private': 'Private - Var% PL Multimercados',
    'Evolução_Percentual_Acumulada_Var%_PL_Total_Ações_Private': 'Private - Var% PL Ações',
    'Evolução_Percentual_Acumulada_Var%_PL_Total_Cambial_Private': 'Private - Var% PL Cambial',
        
    'Evolução_Percentual_Acumulada_Var%_Total': 'Mercado Agregado - Var% PL Total Fundos',
    'Evolução_Percentual_Acumulada_Var%_Mercado_PL_Renda_Fixa': 'Mercado Agregado - Var% PL Renda Fixa',
    'Evolução_Percentual_Acumulada_Var%_Mercado_PL_Ações': 'Mercado Agregado - Var% PL Ações ',
    'Evolução_Percentual_Acumulada_Var%_Mercado_PL_Multimercado': 'Mercado Agregado - Var% PL Multimercado',
    'Evolução_Percentual_Acumulada_Var%_Mercado_PL_Cambial': 'Mercado Agregado - Var% PL Cambial',
    'Evolução_Percentual_Acumulada_Var%_Mercado_PL_ETF': 'Mercado Agregado - Var% PL ETF',
    'Evolução_Percentual_Acumulada_Var%_Mercado_PL_FIDC': 'Mercado Agregado - Var% PL FIDC ',
    'Evolução_Percentual_Acumulada_Var%_Mercado_PL_FIP': 'Mercado Agregado - Var% PL FIP',
    'Evolução_Percentual_Acumulada_Var%_Mercado_PL_FII': 'Mercado Agregado - Var% PL FII',
    'Evolução_Percentual_Acumulada_Var%_Mercado_PL_Off_shore': 'Mercado Agregado - Var% PL Off shore',
    
    'Evolução_Percentual_Acumulada_Var%_Dólar': 'Dólar - Var% Acumulada',
    
    'Evolução_Percentual_Acumulada_Var%_Ibovespa': 'Ibovespa - Var% Acumulada',
    
    'Evolução_Percentual_Acumulada_Var%_Selic': 'Selic - Var% Acumulada'
}

# Extraindo as colunas de evolução percentual acumulada disponíveis para seleção
opcoes_colunas_evolucao_private_resumidas = [value for key, value in mapeamento_colunas_resumidas.items() if key in Totalizadores_Dados_Fundos_Private.columns]
opcoes_colunas_evolucao_mercado_resumidas = [value for key, value in mapeamento_colunas_resumidas.items() if key in PL_Por_Classe_Dados_Mercado_Fundos.columns]
opcoes_colunas_evolucao_dolar_resumidas = [value for key, value in mapeamento_colunas_resumidas.items() if key in Historico_Dolar.columns]
opcoes_colunas_evolucao_ibovespa_resumidas = [value for key, value in mapeamento_colunas_resumidas.items() if key in Historico_Ibovespa.columns]
opcoes_colunas_evolucao_selic_resumidas = [value for key, value in mapeamento_colunas_resumidas.items() if key in Historico_Selic.columns]

# Criando a lista final de opções para o multiselect, incluindo as colunas de evolução percentual acumulada
opcoes_colunas_private_com_evolucao_resumidas = opcoes_colunas_evolucao_private_resumidas
opcoes_colunas_mercado_com_evolucao_resumidas = opcoes_colunas_evolucao_mercado_resumidas
opcoes_colunas_evolucao_benchs_resumidas = (opcoes_colunas_evolucao_dolar_resumidas + 
                                            opcoes_colunas_evolucao_ibovespa_resumidas + 
                                            opcoes_colunas_evolucao_selic_resumidas)


colunas_selecionadas_private = st.sidebar.multiselect('Private Banking', opcoes_colunas_evolucao_private_resumidas)
colunas_selecionadas_mercado = st.sidebar.multiselect('Mercado Agregado', opcoes_colunas_mercado_com_evolucao_resumidas)
colunas_selecionadas_benchs = st.sidebar.multiselect('Benchmark', opcoes_colunas_evolucao_benchs_resumidas)

# Inicializar a variável dados_bench com um DataFrame vazio
dados_bench = pd.DataFrame()

if colunas_selecionadas_private or colunas_selecionadas_mercado or colunas_selecionadas_benchs:
    # Gerar o gráfico de linha com os dados selecionados
    fig, ax = plt.subplots(figsize=(10, 6))
    plotted_private = False
    plotted_market = False
    
    # Plotar os dados dos fundos private
    for coluna in colunas_selecionadas_private:
        coluna_original = [key for key, value in mapeamento_colunas_resumidas.items() if value == coluna][0]
        sns.lineplot(data=Totalizadores_Dados_Fundos_Private, x='Data', y=coluna_original, label=coluna, ax=ax)
        plotted_private = True
        break
    
    # Plotar os dados dos fundos de mercado
    for coluna in colunas_selecionadas_mercado:
        coluna_original = [key for key, value in mapeamento_colunas_resumidas.items() if value == coluna][0]
        sns.lineplot(data=PL_Por_Classe_Dados_Mercado_Fundos, x='Data', y=coluna_original, label=coluna, ax=ax)
        plotted_market = True
        break
    
    # Verificar se há colunas de benchmark selecionadas
    if colunas_selecionadas_benchs:
        for coluna in colunas_selecionadas_benchs:
            if coluna in opcoes_colunas_evolucao_dolar_resumidas: 
                dados_bench = Historico_Dolar
            elif coluna in opcoes_colunas_evolucao_ibovespa_resumidas:
                dados_bench = Historico_Ibovespa
            elif coluna in opcoes_colunas_evolucao_selic_resumidas:
                dados_bench = Historico_Selic
                
            coluna_original = [key for key, value in mapeamento_colunas_resumidas.items() if value == coluna][0]
            sns.lineplot(data=dados_bench, x='Data', y=coluna_original, label=f"Bench - {coluna}", ax=ax)
            break

    if plotted_private:
        ax.set_title('Comportamento Fundos de Investimento (Private)', fontsize=16, pad=20, fontweight='bold', color='white')
    elif plotted_market:
        ax.set_title('Comportamento Fundos de Investimento (Mercado)', fontsize=16, pad=20, fontweight='bold', color='white')
        
    ax.set_ylabel('Evolução % Acumulada', fontsize=12, color='white')
    
    legend = ax.legend(loc='upper left', fontsize=10, bbox_to_anchor=(0.05, 0.95))
    for text in legend.get_texts():
        text.set_color('black')
    
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.tick_params(axis='both', labelsize=10, colors='white')
    ax.xaxis.label.set_rotation(45)
    ax.xaxis.set_tick_params(rotation=45, colors='white')
    ax.yaxis.labelpad = 20
    ax.xaxis.labelpad = 20
    ax.set_facecolor('whitesmoke')
    plt.tight_layout()
    
    # Alterando a cor externa do gráfico para cinza escuro
    fig.set_facecolor('#333333')
    
    st.pyplot(fig)  # Exibir o gráfico de linha usando st.pyplot()

# Verificar se há colunas de benchmark selecionadas
if colunas_selecionadas_benchs:
    dados_bench = pd.DataFrame()
    # Criar uma lista para armazenar as colunas de benchmark selecionadas
    colunas_selecionadas_benchs_final = []
    for coluna in colunas_selecionadas_benchs:
        # Verificar se a coluna é relacionada ao Dólar
        if coluna in opcoes_colunas_evolucao_dolar_resumidas:
            # Adicionar apenas a primeira ocorrência da coluna relacionada ao Dólar
            if "Dólar" not in colunas_selecionadas_benchs_final:
                dados_bench = pd.concat([dados_bench, Historico_Dolar], axis=1)
                colunas_selecionadas_benchs_final.append("Dólar")
        elif coluna in opcoes_colunas_evolucao_ibovespa_resumidas:
            dados_bench = pd.concat([dados_bench, Historico_Ibovespa], axis=1)
        elif coluna in opcoes_colunas_evolucao_selic_resumidas:
            dados_bench = pd.concat([dados_bench, Historico_Selic], axis=1)
        else:
            colunas_selecionadas_benchs_final.append(coluna)

    # Remover a coluna 'Data' dos dados do benchmark
    dados_bench = dados_bench.drop(columns=['Data'], errors='ignore')

    # Adicionar as colunas de benchmark selecionadas corretamente
    colunas_selecionadas_benchs_final.extend([coluna for coluna in colunas_selecionadas_benchs if coluna not in opcoes_colunas_evolucao_dolar_resumidas])

# Calcular a matriz de correlação apenas se houver colunas selecionadas para os dados private e de mercado
if colunas_selecionadas_private and colunas_selecionadas_mercado:
    # Verificar se as colunas selecionadas estão presentes nos dados private e de mercado
    colunas_private_presentes = [key for key, value in mapeamento_colunas_resumidas.items() if value in colunas_selecionadas_private]
    colunas_mercado_presentes = [key for key, value in mapeamento_colunas_resumidas.items() if value in colunas_selecionadas_mercado]

    # Filtrar apenas as colunas presentes nos dados
    dados_selecionados_private = Totalizadores_Dados_Fundos_Private[colunas_private_presentes].copy()
    dados_selecionados_mercado = PL_Por_Classe_Dados_Mercado_Fundos[colunas_mercado_presentes].copy()

    # Combinar os dados selecionados com os dados do benchmark
    dados_selecionados = pd.concat([dados_selecionados_private, dados_selecionados_mercado], axis=1)

    # Verificar se há colunas de benchmark selecionadas
    if colunas_selecionadas_benchs:
        # Combinar os dados selecionados com os dados do benchmark
        if not dados_bench.empty:
            dados_selecionados = pd.concat([dados_selecionados, dados_bench], axis=1)

    # Renomear as colunas da matriz de correlação
    dados_selecionados.columns = [mapeamento_colunas_resumidas.get(coluna, coluna) for coluna in dados_selecionados.columns]

    # Calcular a matriz de correlação apenas se houver dados selecionados
    if not dados_selecionados.empty:
        # Calcular a matriz de correlação
        matriz_correlacao = dados_selecionados.corr()

        
        # Plotar o mapa de calor da matriz de correlação
        fig_corr, ax_corr = plt.subplots(figsize=(10, 6))  # Criar uma nova figura para a matriz de correlação
        heatmap = sns.heatmap(matriz_correlacao, annot=True, cmap='coolwarm', fmt=".2f", vmin=-1, vmax=1, ax=ax_corr)

# Ajustar a cor do texto na barra de cores para branco
        cbar = heatmap.collections[0].colorbar
        cbar.ax.yaxis.set_tick_params(color='white')  # Define a cor dos marcadores da barra de cores para branco
        cbar.ax.tick_params(colors='white')  # Define a cor do texto na barra de cores para branco

        # Configurar título e rótulos dos eixos
        ax_corr.set_title('Matriz de Correlação', fontsize=16, pad=20, fontweight='bold', color='white')
        ax_corr.set_xticklabels(ax_corr.get_xticklabels(), rotation=45, color='white')  # Rotacionar os rótulos do eixo x
        ax_corr.set_yticklabels(ax_corr.get_yticklabels(), color='white')  # Alterar a cor dos rótulos do eixo y
        ax_corr.tick_params(axis='both', labelsize=10, colors='white')  # Alterar a cor dos rótulos dos eixos x e y

        ax_corr.set_xlabel(ax_corr.get_xlabel(), fontsize=10, color='white', labelpad=-10)  # Ajustar o rótulo do eixo x
        plt.xticks(rotation=45, ha='right')  # Ajustar a rotação e o alinhamento horizontal dos marcadores do eixo x


        # Alterando a cor externa da matriz de correlação para cinza escuro
        fig_corr.set_facecolor('#333333')

        st.pyplot(fig_corr)  # Exibir a matriz de correlação usando st.pyplot()
else:
    st.warning("Por favor, selecione pelo menos uma classe de Fundos para visualização.")