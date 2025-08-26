import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Defina a semente para reprodutibilidade
np.random.seed(42)

# Parâmetros para geração de dados
num_vendas = 10000  # 10.000 linhas
produtos = [f'Produto_{i}' for i in range(1, 51)]  # 50 produtos diferentes
categorias = ['Eletrônicos', 'Roupas', 'Alimentos', 'Ferramentas', 'Decoração']
cidades = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Porto Alegre', 'Salvador']

# Gere a data de forma aleatória nos últimos 3 anos
data_inicio = datetime.now() - timedelta(days=3 * 365)
datas = [data_inicio + timedelta(days=np.random.randint(0, 3 * 365)) for _ in range(num_vendas)]

# Crie o DataFrame
df = pd.DataFrame({
    'ID_Venda': np.arange(1, num_vendas + 1),
    'Data_Venda': datas,
    'Produto': np.random.choice(produtos, num_vendas),
    'Categoria': np.random.choice(categorias, num_vendas),
    'Preco_Unitario': np.random.uniform(5.0, 500.0, num_vendas).round(2),
    'Quantidade': np.random.randint(1, 10, num_vendas),
    'Cidade': np.random.choice(cidades, num_vendas),
    'ID_Cliente': np.random.randint(1000, 2000, num_vendas)
})

# Calcule o total de vendas
df['Total_Venda'] = df['Preco_Unitario'] * df['Quantidade']

# Salve o DataFrame em um arquivo CSV na pasta raw
df.to_csv('sales_data.csv', index=False)

print("Arquivo 'sales_data.csv' criado com sucesso na pasta data/raw/")