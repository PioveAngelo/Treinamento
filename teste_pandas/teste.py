import pandas as pd

data = {'Name' : ['Alice', 'Bob', 'Charlie'], 
        'Age' : [25, 30, 35],
        'City' : ['Curitiba', 'São Paulo', 'Belém']}

df = pd.DataFrame(data)

print(df)