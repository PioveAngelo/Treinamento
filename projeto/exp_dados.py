import pandas as pd

dados = {
    'Nome' : ['Angelo', 'Emmy'],
    'Email' : ['angelopiovezan15@gmail.com', 'emmyetsc@gmail.com'],
    'Produto' : ['TV', 'Air Fryer'],
    'Quantidade' : [2, 3],
    'Valor Unitário' : [1500.00, 490.00]
}

df = pd.DataFrame(dados)
df.to_excel('dados_clientes.xlsx', index=False)

print("Dados salvos com sucesso em 'dados_clientes.xlsx'")

dados2 = {
    'Campo' : ['Nome do Cliente', 'Email', 'Produto', 'Quantidade', 'Valor Unitário', 'Valor Total'],
    'Valor' : ['','','','','','']
}

df2 = pd.DataFrame(dados2)
df2.to_excel('modelo_nota.xlsx', index=False)