# Importe as bibliotecas
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 


# leia os conjuntos de dados em DataFrames

orders = pd.read_csv('/datasets/instacart_orders.csv', delimiter=';')
products = pd.read_csv('/datasets/products.csv', delimiter=';')
aisles = pd.read_csv('/datasets/aisles.csv', delimiter=';')
departments = pd.read_csv('/datasets/departments.csv', delimiter=';')
order_products = pd.read_csv('/datasets/order_products.csv', delimiter=';')

# imprima as informações sobre o DataFrame
print(orders.info())


# imprima as informações sobre o DataFrame
print(products.info())


# imprima as informações sobre o DataFrame
print(aisles.info())


# imprima as informações sobre o DataFrame
print(departments.info())

# imprima as informações sobre o DataFrame
print(order_products.info())


# Algumas conclusões intermediárias:
# 
# 1.O DataFrame `orders` tem 478.967 linhas e 6 colunas. Existem algumas entradas nulas na coluna `days_since_prior_order`.
# 
# 2.O DataFrame `products` tem 49.694 linhas e 4 colunas. Existem algumas entradas nulas na coluna `product_name`.
# 
# 3.O DataFrame `aisles` tem 134 linhas e 2 colunas. Não há entradas nulas.
# 
# 4.O DataFrame `departments` tem 21 linhas e 2 colunas. Não há entradas nulas.
# 
# 5.O DataFrame `order_products` tem 4.545.007 linhas e 4 colunas. Não há entradas nulas.
# 
# Parece que a maioria dos DataFrames não contém entradas nulas, exceto pelos DataFrames `orders` e `products`. Isso é algo que deve-se investigar mais para entender por que esses valores estão faltando e se é necessário lidar com esses valores ausentes de alguma forma.

# # Etapa 2. Preparação de dados

# Verificar se há pedidos duplicados

duplicated_rows = orders.duplicated()

# Filtrar as linhas duplicadas
duplicated_orders = orders[duplicated_rows]

print("Número de linhas duplicadas no DataFrame 'orders':", duplicated_orders.shape[0])

if duplicated_orders.shape[0] > 0:
    # Verificar quais colunas são iguais nas linhas duplicadas
    cols_equal = (duplicated_orders == duplicated_orders.iloc[0]).all()

    print("Colunas que são iguais nas linhas duplicadas:")
    print(cols_equal[cols_equal])
    print(orders[orders.duplicated()])



# verifique todos os pedidos feitos às 2h da manhã nas quartas-feiras
orders_quarta_2h = orders[(orders['order_dow'] == 3) & (orders['order_hour_of_day'] == 2)]

print("Número de pedidos feitos às 2h da manhã nas quartas-feiras:", orders_quarta_2h.shape[0])


# Remova pedidos duplicados
orders.drop_duplicates(inplace=True)


# Verifique as linhas duplicadas mais uma vez
duplicated_rows = orders.duplicated()
num_duplicated_rows = duplicated_rows.sum()

print("Número de linhas duplicadas no DataFrame 'orders':", num_duplicated_rows)


# Verifique novamente apenas os IDs de pedidos duplicados
duplicated_order_ids = orders['order_id'][orders.duplicated('order_id')]

print("Número de IDs de pedidos duplicados:", duplicated_order_ids.shape[0])
print("IDs de pedidos duplicados:", duplicated_order_ids.unique())


# Verifique se há linhas completamente duplicadas
duplicated_products = products.duplicated()

# Contar o número de linhas duplicadas
num_duplicated_products = duplicated_products.sum()

print("Número de linhas completamente duplicadas no DataFrame 'products':", num_duplicated_products)


# Verifique apenas se há IDs dos produtos duplicados
duplicated_product_ids = products['product_id'][products.duplicated('product_id')]

# Contar o número de IDs de produtos duplicados
num_duplicated_product_ids = duplicated_product_ids.shape[0]

# Imprimir o número de IDs de produtos duplicados e os IDs duplicados
print("Número de IDs de produtos duplicados:", num_duplicated_product_ids)
if num_duplicated_product_ids > 0:
    print("IDs de produtos duplicados:", duplicated_product_ids.unique())


# Verifique apenas se há nomes de produtos duplicados (converta os nomes para minúsculas para uma comparação melhor)
# Converter os nomes dos produtos para minúsculas
products['product_name'] = products['product_name'].str.lower()

# Verificar se há nomes de produtos duplicados no DataFrame 'products'
duplicated_product_names = products['product_name'][products.duplicated('product_name')]

# Contar o número de nomes de produtos duplicados
num_duplicated_product_names = duplicated_product_names.shape[0]

# Imprimir o número de nomes de produtos duplicados e os nomes duplicados
print("Número de nomes de produtos duplicados:", num_duplicated_product_names)
if num_duplicated_product_names > 0:
    print("Nomes de produtos duplicados:", duplicated_product_names.unique())


# Verifique os nomes de produtos duplicados que não estão faltando

# Converter os nomes dos produtos para minúsculas
products['product_name'] = products['product_name'].str.lower()

# Remover linhas com nomes de produtos faltando
products_non_missing = products.dropna(subset=['product_name'])

# Verificar se há nomes de produtos duplicados no DataFrame 'products'
duplicated_product_names = products_non_missing['product_name'][products_non_missing.duplicated('product_name')]

# Contar o número de nomes de produtos duplicados
num_duplicated_product_names = duplicated_product_names.shape[0]

# Imprimir o número de nomes de produtos duplicados e os nomes duplicados
print("Número de nomes de produtos duplicados (não faltando):", num_duplicated_product_names)
if num_duplicated_product_names > 0:
    print("Nomes de produtos duplicados (não faltando):", duplicated_product_names.unique())


# Verifique se há linhas completamente duplicadas
duplicated_departments = departments.duplicated()

# Contar o número de linhas duplicadas
num_duplicated_departments = duplicated_departments.sum()

print("Número de linhas completamente duplicadas no DataFrame 'departments':", num_duplicated_departments)


# Verifique apenas se há IDs dos produtos duplicados
duplicated_department_ids = departments['department_id'][departments.duplicated('department_id')]

# Contar o número de IDs de departamentos duplicados
num_duplicated_department_ids = duplicated_department_ids.shape[0]

# Imprimir o número de IDs de departamentos duplicados e os IDs duplicados
print("Número de IDs de departamentos duplicados:", num_duplicated_department_ids)
if num_duplicated_department_ids > 0:
    print("IDs de departamentos duplicados:", duplicated_department_ids.unique())


# Verifique se há linhas completamente duplicadas
duplicated_aisles = aisles.duplicated()

# Contar o número de linhas duplicadas
num_duplicated_aisles = duplicated_aisles.sum()

print("Número de linhas completamente duplicadas no DataFrame 'aisles':", num_duplicated_aisles)


# Verifique apenas se há IDs dos produtos duplicados
duplicated_aisle_ids = aisles['aisle_id'][aisles.duplicated('aisle_id')]

# Contar o número de IDs (aisles) duplicados
num_duplicated_aisle_ids = duplicated_aisle_ids.shape[0]

# Imprimir o número de IDs (aisles) duplicados e os IDs duplicados
print("Número de IDs de corredores (aisles) duplicados:", num_duplicated_aisle_ids)
if num_duplicated_aisle_ids > 0:
    print("IDs de corredores (aisles) duplicados:", duplicated_aisle_ids.unique())


# Verifique se há linhas completamente duplicadas
duplicated_order_products = order_products.duplicated()

# Contar o número de linhas duplicadas
num_duplicated_order_products = duplicated_order_products.sum()

print("Número de linhas completamente duplicadas no DataFrame 'order_products':", num_duplicated_order_products)


# Verifique mais uma vez se há outros casos complicados de duplicados
duplicated_order_products_combination = order_products.duplicated(subset=['order_id', 'product_id', 'add_to_cart_order'])

# Contar o número de duplicatas
num_duplicated_order_products_combination = duplicated_order_products_combination.sum()

print("Número de duplicatas considerando uma combinação de colunas no DataFrame 'order_products':", num_duplicated_order_products_combination)


# Encontre valores ausentes na coluna 'product_name'
missing_product_name = products['product_name'].isnull()

# Contar o número de valores ausentes
num_missing_product_name = missing_product_name.sum()

print("Número de valores ausentes na coluna 'product_name' no DataFrame 'products':", num_missing_product_name)


# Filtrar linhas com nomes de produtos ausentes
missing_product_name_rows = products[products['product_name'].isnull()]

# Verificar se todos os nomes de produtos ausentes estão associados com a seção de ID 100
all_missing_names_aisle_100 = missing_product_name_rows['aisle_id'].eq(100).all()

print("Todos os nomes de produtos ausentes estão associados com a seção de ID 100:", all_missing_names_aisle_100)

# Verificar se há produtos com nomes ausentes que não estão associados à seção de ID 100
missing_names_not_aisle_100 = products[products['product_name'].isna()], products[(products['product_name'].isna()) & (products['aisle_id'] != 100)]

print("Produtos com nomes ausentes que não estão associados à seção de ID 100:")
print(missing_names_not_aisle_100)


# Todos os nomes de produtos ausentes estão associados com o departamento de ID 21?
# Fazer a junção entre 'products' e 'aisles'
products_with_department = pd.merge(products, aisles, on='aisle_id')

# Filtrar linhas com nomes de produtos ausentes
missing_product_name_rows = products_with_department[products_with_department['product_name'].isnull()]

# Verificar se todos os nomes de produtos ausentes estão associados com o departamento de ID 21
all_missing_names_department_21 = missing_product_name_rows['department_id'].eq(21).all()

print("Todos os nomes de produtos ausentes estão associados com o departamento de ID 21:", all_missing_names_department_21)


# Use as tabelas de departamentos e seções para verificar os dados da seção ID 100 e do departamento ID 21.
# Combinando as tabelas de produtos, seções e departamentos
merged_data = pd.merge(products, aisles, on='aisle_id')
merged_data = pd.merge(merged_data, departments, on='department_id')

# Filtrar para seção ID 100
aisle_100_data = merged_data.query('aisle_id == 100')

# Filtrar para departamento ID 21
department_21_data = merged_data.query('department_id == 21')

# Exibir resultados
print("Dados da seção ID 100:")
print(aisle_100_data.head())
print("\nDados do departamento ID 21:")
print(department_21_data.head())


# Preencher nomes de produtos ausentes com 'Unknown'
products['product_name'] = products['product_name'].fillna('Unknown')

# Verificar se ainda há valores ausentes na coluna 'product_name'
missing_product_name = products['product_name'].isnull().sum()

print("Número de valores ausentes na coluna 'product_name' após preenchimento:", missing_product_name)

# Encontre os valores ausentes
missing_values_orders = orders.isnull().sum()

print("Número de valores ausentes em cada coluna do DataFrame 'orders':")
print(missing_values_orders)


# Filtrar para clientes que não estão fazendo o primeiro pedido
not_first_order = orders.query('order_number > 1')

# Verificar valores ausentes para esses clientes na coluna 'days_since_prior_order'
missing_values_not_first_order = not_first_order['days_since_prior_order'].isnull().sum()

print("Número de valores ausentes para clientes que não estão fazendo o primeiro pedido:", missing_values_not_first_order)


# Encontre os valores ausentes
missing_values_order_products = order_products.isnull().sum()

print("Número de valores ausentes em cada coluna do DataFrame 'order_products':")
print(missing_values_order_products)


# Quais são os valores mínimo e máximo dessa coluna?
# Encontrar valores mínimo e máximo na coluna 'days_since_prior_order'
min_days_since_prior_order = orders['days_since_prior_order'].min()
max_days_since_prior_order = orders['days_since_prior_order'].max()

print("Valor mínimo na coluna 'days_since_prior_order':", min_days_since_prior_order)
print("Valor máximo na coluna 'days_since_prior_order':", max_days_since_prior_order)


 
# Salve todos os IDs dos pedidos com pelo menos um valor ausente em 'add_to_cart_order'
order_ids_with_missing_add_to_cart_order = order_products.query('add_to_cart_order.isnull()', engine='python')['order_id'].unique()

# Salvar os IDs dos pedidos em um arquivo
np.savetxt('order_ids_with_missing_add_to_cart_order.txt', order_ids_with_missing_add_to_cart_order, fmt='%d')


# Agrupar por ID do pedido e contar o número de 'product_id' em cada pedido
product_count_per_order = order_products.groupby('order_id')['product_id'].count()

# Filtrar IDs dos pedidos com pelo menos um valor ausente em 'add_to_cart_order'
order_ids_with_missing_add_to_cart_order = order_products.query('add_to_cart_order.isnull()', engine='python')['order_id'].unique()

# Verificar o valor mínimo da contagem para os pedidos com dados ausentes
min_product_count = product_count_per_order.loc[order_ids_with_missing_add_to_cart_order].min()

print("Valor mínimo da contagem de produtos para os pedidos com valores ausentes:", min_product_count)


# Substitua valores ausentes na coluna 'add_to_cart_order' por 999 e converta a coluna para o tipo integer

# Substituir valores ausentes em 'add_to_cart_order' por 999
order_products['add_to_cart_order'] = order_products['add_to_cart_order'].fillna(999)

# Converter 'add_to_cart_order' para tipo inteiro
order_products['add_to_cart_order'] = order_products['add_to_cart_order'].astype(int)

print(order_products.info())
print(order_products.head())


# Verificar estatísticas descritivas da coluna 'order_hour_of_day'
print(orders['order_hour_of_day'].describe())



# Verificar estatísticas descritivas da coluna 'order_dow'
print(orders['order_dow'].describe())


# Verificar os valores únicos na coluna 'order_hour_of_day'
unique_order_hour_of_day = orders['order_hour_of_day'].unique()
print("Valores únicos na coluna 'order_hour_of_day':", unique_order_hour_of_day)

# Verificar os valores únicos na coluna 'order_dow'
unique_order_dow = orders['order_dow'].unique()
print("Valores únicos na coluna 'order_dow':", unique_order_dow)


# Plotar a distribuição de 'order_hour_of_day'
import matplotlib.pyplot as plt
plt.hist(orders['order_hour_of_day'], bins=24, range=(0, 23))
plt.title("Distribuição de 'order_hour_of_day'")
plt.xlabel('Hour of Day')
plt.ylabel('Count')
plt.show()


# Plotar a distribuição de 'order_dow'
plt.hist(orders['order_dow'], bins=7, range=(0, 6))
plt.title("Distribuição de 'order_dow'")
plt.xlabel('Day of Week')
plt.ylabel('Count')
plt.show()


# Contar o número de pedidos por hora do dia
orders_per_hour = orders['order_hour_of_day'].value_counts().sort_index()

# Criar um gráfico de barras
plt.figure(figsize=(10, 6))
orders_per_hour.plot(kind='bar')
plt.title('Número de Pedidos por Hora do Dia')
plt.xlabel('Hora do Dia')
plt.ylabel('Número de Pedidos')
plt.xticks(rotation=0)
plt.show()


# Mapear os valores numéricos para os nomes dos dias da semana
dow_mapping = {0: 'Domingo', 1: 'Segunda-feira', 2: 'Terça-feira', 3: 'Quarta-feira', 4: 'Quinta-feira', 5: 'Sexta-feira', 6: 'Sábado'}

# Substituir os valores numéricos pelos nomes dos dias da semana
orders['order_dow'] = orders['order_dow'].replace(dow_mapping)

# Contar o número de pedidos por dia da semana
orders_per_day = orders['order_dow'].value_counts().reindex(dow_mapping.values())

# Criar um gráfico de barras
plt.figure(figsize=(10, 6))
orders_per_day.plot(kind='bar')
plt.title('Número de Pedidos por Dia da Semana')
plt.xlabel('Dia da Semana')
plt.ylabel('Número de Pedidos')
plt.xticks(rotation=45)
plt.show()


# Eliminar valores nulos em 'days_since_prior_order'
days_since_prior_order = orders['days_since_prior_order'].dropna()

# Criar um histograma
plt.figure(figsize=(10, 6))
plt.hist(days_since_prior_order, bins=30, edgecolor='k')
plt.title('Distribuição do Tempo até o Próximo Pedido')
plt.xlabel('Dias até o Próximo Pedido')
plt.ylabel('Frequência')
plt.show()


# Definir quarta-feira como 2 e sábado como 5
wednesday = 2
saturday = 5

# Filtrar os pedidos feitos nas quartas-feiras e sábados
wednesday_orders = orders[orders['order_dow'] == 'Quarta-feira']
saturday_orders = orders[orders['order_dow'] == 'Sábado']

# Calcular a contagem de pedidos para cada hora do dia nas quartas e sábados
wednesday_order_counts = wednesday_orders['order_hour_of_day'].value_counts().sort_index()
saturday_order_counts = saturday_orders['order_hour_of_day'].value_counts().sort_index()

# Criar o gráfico
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.bar(wednesday_order_counts.index, wednesday_order_counts.values, color='blue', alpha=0.75)
plt.title('Orders on Wednesday')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Orders')

plt.subplot(1, 2, 2)
plt.bar(saturday_order_counts.index, saturday_order_counts.values, color='red', alpha=0.75)
plt.title('Orders on Saturday')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Orders')

plt.tight_layout()
plt.show()



print(wednesday_order_counts)

print(saturday_order_counts)


print(wednesday_orders)


print(saturday_orders)


orders['order_dow'].unique()


# Contar o número de pedidos para cada cliente
orders_per_customer = orders['user_id'].value_counts()

# Contar o número de clientes para cada número de pedidos
customers_per_orders = orders_per_customer.value_counts()

# Plotar um gráfico de barras
customers_per_orders.plot.bar()
plt.xlabel('Number of Orders')
plt.ylabel('Number of Customers')
plt.title('Distribution of Number of Orders per Customer')
plt.show()


# Contar a frequência de cada product_id em order_products
product_counts = order_products['product_id'].value_counts()


# Pegar os 20 primeiros product_ids
top_20_product_ids = product_counts.head(20).index


# Usar os product_ids para obter os nomes dos produtos em products
top_20_products = products[products['product_id'].isin(top_20_product_ids)]

# Exibir os IDs e nomes dos produtos
print(top_20_products[['product_id', 'product_name']])

 

df_merge = order_products.merge(products, on='product_id')
top_products = df_merge.groupby(['product_id', 'product_name']).count().sort_values(['order_id'], ascending=False)

# Criar o gráfico de barras
ax = top_products.head(20).plot.bar(y='order_id', legend=False)

# Adicionar rótulos ao gráfico
ax.set_xlabel('Produto')
ax.set_ylabel('Número de Pedidos')
ax.set_title('Top 20 Produtos Mais Populares')

# Girar os rótulos do eixo x para melhor legibilidade
ax.tick_params(axis='x', rotation=90)

# Mostrar o gráfico
plt.show()



order_item_counts = order_products.groupby('order_id').size()


# Calcula a média de itens por pedido
mean_items_per_order = order_item_counts.mean()


# Obtém a distribuição de itens por pedido
distribution = order_item_counts.value_counts()

print("Média de itens por pedido:", mean_items_per_order)
print("Distribuição de itens por pedido:")
print(distribution)


num_items = order_products.groupby('order_id').count()['product_id']
histogram_vals = num_items.value_counts().sort_index()

# Criar o histograma
histogram_vals.plot(kind='bar',
                title='Items purchased in one order',
                xlabel='Number of items',
                ylabel='Number of orders'
               )

# Mostrar o histograma
plt.show()


# Agrupar pelo 'product_id' e somar a coluna 'reordered'
top_reordered = order_products.groupby('product_id')['reordered'].sum()


# Ordenar em ordem decrescente
top_reordered = top_reordered.sort_values(ascending=False)


# Obter os 20 principais produtos reordenados
top_20_reordered = top_reordered.head(20)


# Obter os nomes dos produtos
top_20_reordered_names = top_20_reordered.reset_index().merge(products, on='product_id')

# Exibir os IDs e nomes dos produtos
print(top_20_reordered_names[['product_id', 'product_name']])



# Plotar o gráfico
top_20_reordered_names.plot(kind='bar', x='product_name', y='product_id', legend=None)
plt.title('Top 20 most frequently included items in repeated orders')
plt.xlabel('Product Name')
plt.ylabel('Number of Times Included')
plt.xticks(rotation=45, ha='right')
plt.show()


# Juntar os DataFrames para obter os nomes dos produtos
order_products_with_names = order_products.merge(products, on='product_id')




# Calcular a proporção de pedidos repetidos para cada produto
product_reorder_ratio = order_products_with_names.groupby(['product_id', 'product_name'])['reordered'].mean().reset_index()




# Renomear colunas para maior clareza
product_reorder_ratio.columns = ['product_id', 'product_name', 'reorder_ratio']

# Exibir as primeiras linhas da tabela
print(product_reorder_ratio.head())




# Filtrar os 20 produtos com maior proporção de pedidos repetidos
top_20_reorder_ratio = product_reorder_ratio.sort_values('reorder_ratio', ascending=False).head(20)

# Plotar o gráfico
top_20_reorder_ratio.plot(kind='bar', x='product_name', y='reorder_ratio', legend=None)
plt.title('Top 20 products with the highest reorder ratio')
plt.xlabel('Product Name')
plt.ylabel('Reorder Ratio')
plt.xticks(rotation=45, ha='right')
plt.show()


# Combinar as informações do DataFrame 'orders' e 'order_products'
merged = pd.merge(order_products, orders, on='order_id')

# Agrupar por user_id e order_id
grouped = merged.groupby(['user_id', 'order_id'])

# Calcular o total de pedidos e pedidos repetidos para cada cliente
order_counts = grouped.size().reset_index(name='total_orders')
reordered_counts = grouped['reordered'].sum().reset_index(name='reordered_orders')

# Juntar os dois DataFrames
customer_orders = pd.merge(order_counts, reordered_counts, on=['user_id', 'order_id'])



# Calcular a proporção de pedidos repetidos
customer_orders['reorder_ratio'] = customer_orders['reordered_orders'] / customer_orders['total_orders']

# Agrupar por user_id e calcular a média da proporção de pedidos repetidos
customer_reorder_ratio = customer_orders.groupby('user_id')['reorder_ratio'].mean().reset_index()

print(customer_reorder_ratio.head())



# Filtrar os 20 clientes com maior proporção média de pedidos repetidos
top_20_customer_reorder_ratio = customer_reorder_ratio.sort_values('reorder_ratio', ascending=False).head(20)

# Plotar o gráfico
top_20_customer_reorder_ratio.plot(kind='bar', x='user_id', y='reorder_ratio', legend=None)
plt.title('Top 20 customers with the highest average reorder ratio')
plt.xlabel('User ID')
plt.ylabel('Average Reorder Ratio')
plt.xticks(rotation=45, ha='right')
plt.show()


# Filtra as linhas onde add_to_cart_order é igual a 1
first_added = order_products[order_products['add_to_cart_order'] == 1]


# Conta quantas vezes cada product_id aparece
first_added_counts = first_added['product_id'].value_counts()

# Converte a Series para um DataFrame e redefine o índice
first_added_counts_df = first_added_counts.reset_index()
first_added_counts_df.columns = ['product_id', 'count']



# Junta o resultado com o DataFrame de produtos
result = first_added_counts_df.merge(products, on='product_id')

# Exiba as primeiras 20 linhas
print(result.head(20))


# Ordena o resultado pelo número de vezes que o produto foi o primeiro a ser adicionado ao carrinho
result_sorted = result.sort_values(by='count', ascending=False).head(20)

# Plotar o gráfico
result_sorted.plot(kind='bar', x='product_name', y='count', legend=None)
plt.title('Top 20 items first added to cart')
plt.xlabel('Product Name')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.show()


