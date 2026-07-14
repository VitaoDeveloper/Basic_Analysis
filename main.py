# Análise de Dados com Pandas
#
# Versão simplificada do projeto original: https://github.com/VitaoDeveloper/AI_DataAnalysis

import pandas as pd

# Passo 1 - Importar a base de dados
tabela = pd.read_csv("assets/clientes.csv")

print("=" * 60)
print("PASSO 1 - VISÃO GERAL DA TABELA")
print("=" * 60)
print(tabela.head())
print()
print(tabela.info())

# Passo 2 - Estatísticas descritivas das colunas numéricas
# describe() traz média, desvio padrão, mínimo, máximo e quartis
print("\n" + "=" * 60)
print("PASSO 2 - ESTATÍSTICAS DESCRITIVAS")
print("=" * 60)
print(tabela.describe())

# Passo 3 - Verificar valores nulos por coluna
print("\n" + "=" * 60)
print("PASSO 3 - VALORES NULOS POR COLUNA")
print("=" * 60)
print(tabela.isnull().sum())

# Passo 4 - Distribuição do score de crédito
# value_counts() conta quantas vezes cada valor aparece na coluna
# normalize=True converte a contagem em proporção (%)
print("\n" + "=" * 60)
print("PASSO 4 - DISTRIBUIÇÃO DO SCORE DE CRÉDITO")
print("=" * 60)
print(tabela["score_credito"].value_counts())
print()
print((tabela["score_credito"].value_counts(normalize=True) * 100).round(2).astype(str) + "%")

# Passo 5 - Média de salário anual e dívida total por score de crédito
# groupby() agrupa as linhas por um valor em comum (o score) e permite
# aplicar uma função de agregação (média) sobre as outras colunas
print("\n" + "=" * 60)
print("PASSO 5 - MÉDIAS POR SCORE DE CRÉDITO")
print("=" * 60)
medias_por_score = tabela.groupby("score_credito")[
    ["salario_anual", "divida_total", "num_emprestimos", "dias_atraso"]
].mean()
print(medias_por_score.round(2))

# Passo 6 - Profissões mais comuns entre clientes com score "Good"
print("\n" + "=" * 60)
print("PASSO 6 - PROFISSÕES MAIS COMUNS (SCORE GOOD)")
print("=" * 60)
clientes_bons = tabela[tabela["score_credito"] == "Good"]
print(clientes_bons["profissao"].value_counts().head(10))

# Passo 7 - Correlação entre número de empréstimos e dias de atraso
# corr() calcula o coeficiente de correlação entre colunas numéricas
print("\n" + "=" * 60)
print("PASSO 7 - CORRELAÇÃO ENTRE VARIÁVEIS NUMÉRICAS")
print("=" * 60)
colunas_interesse = ["num_emprestimos", "dias_atraso", "divida_total", "salario_anual"]
print(tabela[colunas_interesse].corr().round(2))

# Passo 8 - Lista de clientes elegíveis a um benefício (score "Good")
# Isso substitui a etapa que antes usava a API da OpenAI para gerar
# um relatório em texto; aqui montamos o "relatório" só com Pandas/Python.
print("\n" + "=" * 60)
print("PASSO 8 - RELATÓRIO DE CLIENTES ELEGÍVEIS AO BENEFÍCIO")
print("=" * 60)

ids_elegiveis = clientes_bons["id_cliente"].unique()
print(f"Total de clientes com score 'Good': {len(ids_elegiveis)}")
print(f"Primeiros 20 IDs elegíveis: {list(ids_elegiveis[:20])}")

# Passo 9 - Salvando o resumo em um novo arquivo CSV
# Assim como no relatório original, aqui geramos um arquivo de saída,
# mas usando apenas recursos do próprio Pandas (to_csv), sem IA.
resumo = pd.DataFrame({
    "id_cliente": ids_elegiveis
})
resumo.to_csv("assets/clientes_elegiveis.csv", index=False)
print("\nArquivo 'assets/clientes_elegiveis.csv' gerado com sucesso.")
