import pandas as pd
import matplotlib.pyplot as plt
dados = {
    "pedido_id": [1,2,3,4,5,6,7,8,9,10,11,12],
    "data": ["2025-01-01","2025-01-02","2025-01-02","2025-01-03","2025-01-04",
             "2025-01-04","2025-01-05","2025-01-06","2025-01-06","2025-01-07",
             "2025-01-08","2025-01-09"],
    "produto": ["Notebook","Mouse","Teclado","Notebook","Mouse",
                "Monitor","Teclado","Notebook","Mouse","Monitor",
                "Notebook","Teclado"],
    "categoria": ["Eletrônicos","Acessórios","Acessórios","Eletrônicos","Acessórios",
                  "Eletrônicos","Acessórios","Eletrônicos","Acessórios","Eletrônicos",
                  "Eletrônicos","Acessórios"],
    "preco": [3000,50,150,3200,50,800,150,3100,60,900,3200,150],
    "quantidade": [1,2,1,1,3,1,2,1,4,1,1,2]
}
df = pd.DataFrame(dados)
#criando separação:
def sep():
    print(35 * '-=-')

#limpeza de dados:
nulos = df.isnull().sum()
duplicados = df.duplicated().sum()
sep()
print('Vendo se os Dados tem Valores Nulos (NaN)\n'
      'Valores Nulos:')
print(nulos)
sep()
print('Vendo se os Dados tem Valores Duplicados\n'
      'Valores Duplicados:')
print(duplicados)
#Criar Colunas:
df['faturamento'] = df['preco'] * df['quantidade']
df['data'] = pd.to_datetime(df['data'])
#Analises:
faturamento_total = df['faturamento'].sum()
sep()
print('Criando uma Coluna nova de Faturamento Total\n'
      'Faturamento Total')
print(faturamento_total)
faturamento_produto = (df.groupby('produto')['faturamento']
                       .sum()
                       .reset_index()
                       .sort_values(by='faturamento', ascending=False))
sep()
print('Criando uma Tabela de Faturamento por Produto\n'
      'Faturamento por Produto:')
print(faturamento_produto)
faturamento_categoria = (df.groupby('categoria')['faturamento']
                         .sum()
                         .reset_index()
                         .sort_values(by='faturamento', ascending=False))
sep()
print('Criando uma Tabela de Faturamento por Categoria\n'
      'Faturamento por Categoria:')
print(faturamento_categoria)
produto_quantidade = (df.groupby('produto')['quantidade']
                        .sum()
                        .reset_index(name='venda')
                        .sort_values(by='venda', ascending=False))
sep()
print('Criando uma Tabela de Produto mais Vendido\n'
      'Produto mais Vendido:')
print(produto_quantidade.head(1))
sep()
print('Criando uma Tabela de Produto que mais Faturou\n'
      'Produto que mais Faturou:')
print(faturamento_produto.head(1))

faturamento_dia = (df.groupby('data')['faturamento']
                   .sum()
                   .reset_index()
                   .sort_values(by='data', ascending=True))
vendas_dia = (df.groupby('data')['quantidade']
              .sum()
              .reset_index(name='venda')
              .sort_values(by='data', ascending=True))

maior_faturamento = faturamento_dia.sort_values(by='faturamento', ascending=False).head(1)
maior_vendas = vendas_dia.sort_values(by='venda', ascending=False).head(1)


sep()
print('Total de Faturamento por Dia\n'
      'Faturamento por Dia:')
print(faturamento_dia)
sep()
print('Dia com o Maior Faturamento\n'
      'Melhor dia de Faturamento:')
print(maior_faturamento)
sep()
print('Dia com o Maior nivel de Vendas\n'
      'Melhor dia de Vendas:')
print(maior_vendas)
#DataFrame:
sep()
print('Tabela atual\n'
      'DataFrame:')
print(df)
#Grafico1:
ax = faturamento_produto.plot(kind='bar', x='produto', y='faturamento', color='lightgreen', figsize=(8,5))
for i, valor in enumerate(faturamento_produto['faturamento']):
    ax.text(i, valor, str(f'R${valor}'), ha='center', va='bottom')
plt.title('Faturamento (R$) por Produto')
plt.xlabel('Produto')
plt.ylabel('Faturamento')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

plt.show()
#Grafico2:
ax2 = faturamento_dia.plot(kind='line', x='data', y='faturamento', color='lightblue', figsize=(8,5), marker='o', linewidth=3)
for i in range(len(faturamento_dia['faturamento'])):
    ax2.text(faturamento_dia['data'].iloc[i],
             faturamento_dia['faturamento'].iloc[i],
             f"R${faturamento_dia['faturamento'].iloc[i]}",
             ha='center',
             va='bottom')
plt.title('Faturamento (R$) por Data')
plt.xlabel('data')
plt.ylabel('faturamento')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

plt.show()
print("\n=== RESUMO FINAL ===")
print(f"Faturamento total: R${faturamento_total}")
print(f"Produto mais vendido: {produto_quantidade.iloc[0]['produto']}")
print(f"Produto mais lucrativo: {faturamento_produto.iloc[0]['produto']}")
print(f"Melhor dia: {maior_faturamento.iloc[0]['data']}")