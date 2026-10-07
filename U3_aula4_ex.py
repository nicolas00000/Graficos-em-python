import sqlite3  #BANCO DE DADOS
import time     #TEMPORIZADOR
import pandas as pd #MEXER COM LISTA E CONTAS JA PRONTAS
import matplotlib.pyplot as plt  #PLOTAGEM DE GRÁFICOS
import seaborn as sns #PLOTAGEM DE GRÁFICOS MAIS BONITOS
from IPython.display import display, HTML



# Passo 1.1: Conectar ao banco de dados (ou criar, se não existir)
conexao = sqlite3.connect('dados_vendas.db')

# Passo 1.2: Criar um cursor
cursor = conexao.cursor()

#apaga o BD e seus ID toda vez q inicia, pq estou inserindo os dados direto do programa 
cursor.execute("DELETE FROM vendas1")
cursor.execute("DELETE FROM sqlite_sequence WHERE name='vendas1'")
conexao.commit()



# Passo 1.3: Criar uma tabela (se não existir)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS vendas1 (
    id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
    data_venda DATE,
    produto TEXT,
    categoria TEXT,
    valor_venda REAL
)
''')

# Passo 1.4: Inserir alguns dados
cursor.execute('''
    INSERT INTO vendas1 (data_venda, produto, categoria, valor_venda) VALUES
        ('2023-01-01', 'Produto A', 'Eletrônicos', 1500.00),
    ('2023-01-05', 'Produto B', 'Roupas', 350.00),
    ('2023-02-10', 'Produto C', 'Eletrônicos', 1200.00),
    ('2023-03-15', 'Produto D', 'Livros', 200.00),
    ('2023-03-20', 'Produto E', 'Eletrônicos', 800.00),
    ('2023-04-02', 'Produto F', 'Roupas', 400.00),
    ('2023-05-05', 'Produto G', 'Livros', 150.00),
    ('2023-06-10', 'Produto H', 'Eletrônicos', 1000.00),
    ('2023-07-20', 'Produto I', 'Roupas', 600.00),
    ('2023-08-25', 'Produto J', 'Eletrônicos', 700.00),
    ('2023-09-30', 'Produto K', 'Livros', 300.00),('2023-03-20', 'Produto E', 'Eletrônicos', 800.00),
    ('2023-04-02', 'Produto F', 'Roupas', 400.00),
    ('2023-05-05', 'Produto G', 'Livros', 150.00),
    ('2023-06-10', 'Produto H', 'Eletrônicos', 1000.00),
    ('2023-07-20', 'Produto I', 'Roupas', 600.00),
    ('2023-08-25', 'Produto J', 'Eletrônicos', 700.00),
    ('2023-09-30', 'Produto K', 'Livros', 300.00),('2023-03-20', 'Produto E', 'Eletrônicos', 800.00),
    ('2023-04-02', 'Produto F', 'Roupas', 400.00),
    ('2023-05-05', 'Produto G', 'Livros', 150.00),
    ('2023-06-10', 'Produto H', 'Eletrônicos', 1000.00),
    ('2023-07-20', 'Produto I', 'Roupas', 600.00),
    ('2023-08-25', 'Produto J', 'Eletrônicos', 700.00),
    ('2023-09-30', 'Produto K', 'Livros', 300.00),
    ('2023-10-05', 'Produto L', 'Roupas', 450.00),
    ('2023-11-15', 'Produto M', 'Eletrônicos', 900.00),
    ('2023-12-20', 'Produto N', 'Livros', 250.00);
''')


def funcoes_crud():
    #SELECT
    # cursor.execute("SELECT * FROM vendas1")
    # dados = cursor.fetchall()   # Guardar os resultados
    # for linha in dados:         # Mostrar os dados
        # print(linha)


    #INSERT
    # cursor.execute("""
    #     INSERT INTO vendas1 (data_venda, produto, categoria, valor_venda)
    #     VALUES (?, ?, ?, ?) """, 
    #     ("2023-12-25", "Produto O", "Eletrônicos", 500))
    # conexao.commit()


    #DELETE
    # cursor.execute("DELETE FROM vendas1 WHERE id_venda = ?", (5,))
    # conexao.commit()


    #UPDATE
    # cursor.execute("""
    #     UPDATE vendas1
    #     SET valor_venda = ?
    #     WHERE id_venda = ?
    # """, (67.67, 4))
    # conexao.commit()


    #SELECT
    # cursor.execute("SELECT * FROM vendas1")
    # dados = cursor.fetchall()   # Guardar os resultados
    # for linha in dados:         # Mostrar os dados
    #     print(linha)
    print("minhas funcoes CRUD")


# ==========================================
# PASSO 2 - EXPLORAR E PREPARAR OS DADOS
# ==========================================

# Carregar os dados da tabela SQLite para um DataFrame
df_vendas = pd.read_sql_query("SELECT * FROM vendas1", conexao)

# Exibir os primeiros registros
print("\n \n \033[91mPrimeiros registros:\033[0m")
print(df_vendas.head(10))
time.sleep(1)

# Informações dos dados 
# (ex: qtd colunas, qtd de itens, tipo: str float, int) 
# E se tem algum dado vazio
print("\n \n \033[91mInformações dos dados:\033[0m")
df_vendas.info()
time.sleep(1)


# Verificar se tem algum dado faltando na tabela 
# (ex: preço, data_da_venda), retorna a qtd de celulas vazias
print("\n \n \033[91mValores vazios:\033[0m")
print(df_vendas.isnull().sum())


# Mostrar algumas estatísticas das vendas
print("\n \033[91mEstatísticas das vendas:\033[0m")
print(df_vendas['valor_venda'].describe().round(2))



# ==========================================
# PASSO 3 - Analise de DADOS individuais
# ==========================================

# Converter a coluna de data para o formato de data
df_vendas['data_venda'] = pd.to_datetime(df_vendas['data_venda'])

#Total das vendas
print("\n \n \033[91mTotal de vendas:\033[0m")
print(df_vendas['valor_venda'].sum().round(2))

#Média das vendas
print("\n \n \033[91mMédia das vendas:\033[0m")
print(df_vendas['valor_venda'].mean().round(2))

#Menor venda
print("\n \n \033[91mMenor venda:\033[0m")
print(df_vendas['valor_venda'].min().round(2))

#Maior venda
print("\n \n \033[91mMaior venda:\033[0m")
print(df_vendas['valor_venda'].max().round(2))



#Total de vendas por categoria             
# O groupby() significa "agrupe todos q forem igual"
# o sum() significa "some todos os valores de cada grupo"
print("\n \n \033[91mValor arrecadado por categoria:\033[0m")        
vendas_por_categoria = df_vendas.groupby('categoria')['valor_venda'].sum().round(2).reset_index(name='Total')
print(vendas_por_categoria.to_string(index=False))



#quantidade de vendas por categoria
print("\n \n \033[91mQuantidade de vendas por categoria:\033[0m")
print(f"\n {df_vendas.groupby('categoria').size()}")



# Converter a coluna de data para o formato de data
df_vendas['data_venda'] = pd.to_datetime(df_vendas['data_venda'])




# ==========================================
# PASSO 4 - VISUALIZAÇÃO DOS GRAFICOS
# ==========================================

plt.figure(figsize=(12, 6)) #TAMANHO DO GRAFICO
plt.subplot(2, 2, 1) # tamanho da tela que vai ser dividido em 4 partes


#1 VENDAS POR CATEGORIA
# Cria o gráfico de barras
sns.barplot(
    data = vendas_por_categoria,
    x="categoria",
    y="Total"
)

#TITULO
plt.title('Total de vendas por categoria')

#TITULO DO EIXOS X
plt.xlabel('Categoria')

#TITULO DO EIXO Y
plt.ylabel('Total de vendas (R$)')

# Mostrar o valor em cima de cada barra
for i, valor in enumerate(vendas_por_categoria['Total']):
    plt.text(i, valor, f'R$ {valor:.0f}', ha='center', va='bottom')

maximo_valor = int(vendas_por_categoria['Total'].max())
plt.ylim(0, maximo_valor + 1000)
plt.yticks(range(0, maximo_valor + 1000, 1000))

# Grade horizontal
plt.grid(axis='y', alpha=0.3)



#2 VENDAS POR TEMPO
plt.subplot(2, 2, 2) # tamanho da tela dividida em 4 e esse é o grafico 2/4

sns.lineplot(
    data = df_vendas,
    x = 'data_venda',
    y = 'valor_venda',
    marker = 'o'  # Adiciona marcadores nos pontos de dados
)

# Adiciona os valores de cada ponto no gráfico
for x, y in zip(df_vendas['data_venda'], df_vendas['valor_venda']):
    plt.text(x, y, f'R$ {y:0.0f}', ha='center', va='bottom')


plt.title('Total de vendas por tempo')
plt.xlabel('Data da Venda')
plt.ylabel('Total de vendas (R$)')

# Limita o eixo Y para melhor visualização
plt.ylim(0, 2000)

# Grade horizontal
plt.grid(axis='y', alpha=0.3)


# Agrupar por categoria e mostrar porcentagem de vendas
plt.subplot(2, 2, 3) # tamanho da tela e esse é o grafico 3/4
vendas_por_categoria_count = df_vendas.groupby('categoria').size()
plt.pie(
    vendas_por_categoria_count.values,
    labels=vendas_por_categoria_count.index,
    autopct='%1.1f%%',  # Mostra a porcentagem
)


plt.title('Quantidade de vendas por categoria')
plt.xlabel('CATEGORIA')
plt.ylabel('VENDAS')


#4 - GRAFICO 4 QUANTIDADE DE CATEGORIA
plt.subplot(2, 2, 4) # tamanho da tela e esse é o grafico 4/4
quantidade_por_categoria = df_vendas.groupby('categoria').size().reset_index(name='Quantidade')

sns.barplot(
    data=quantidade_por_categoria,
    x='categoria',
    y='Quantidade'
)

#Faz a altura do grafico ser automatica com o maior valor da coluna quantidade
plt.yticks(range(0, quantidade_por_categoria['Quantidade'].max() + 5, 5))

plt.title('Quantidade Itens de cada categoria')
plt.xlabel('CATEGORIA')
plt.ylabel('vendas')

# Grade horizontal
plt.grid(axis='y', alpha=0.3)

# Mostrar o valor em cima de cada barra
for i, valor in enumerate(quantidade_por_categoria['Quantidade']):
    plt.text(i, valor, f'{valor}', ha='center', va='bottom')


plt.tight_layout() # Não deixa os gráficos se sobreporem
plt.show()  # Mostra o gráfico