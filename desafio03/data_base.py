import pandas as pd

def data_base():
    data = {
        "produtos": ["Air Fryer", "MICROONDAS", "TV 60 POL", "Liquidificador", "Ventilador", "TV 50 POL"]
    }

    df = pd.DataFrame(data)
    df.to_excel('data_base.xlsx', index=False)
    print("Base de dados criada com sucesso em 'data_base.xlsx'")

    return df

data_base()