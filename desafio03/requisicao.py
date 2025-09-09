import requests
import pandas as pd

api_link = "http://127.0.0.1:8000"

email = "angelopiovezan@email.com"
senha = "Ae06062018@"

login_link = f"{api_link}/auth/login"
login_data = {
    "email": email,
    "senha": senha
}

login = requests.post(login_link, json=login_data)
print(login.status_code)

produtos_planilha = []

df = pd.read_excel('data_base.xlsx')
def pegar_da_planilha(planilha):
    for i, row in planilha.iterrows():
        nome = row["produtos"]
        produtos_planilha.append(str(nome))

pegar_da_planilha(df)

if login.status_code == 200:
    token = login.json()["access_token"]
    print(token)
    print("Autenticado com sucesso!")

    produtos_link = f"{api_link}/products/listar"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }

    produtos_response = requests.get(produtos_link, headers=headers)
    
    if produtos_response.status_code == 200:
        produtos = produtos_response.json()["produtos"]

        def buscar(nome):
            for i in produtos:
                if nome == i["nome"]:
                    return i
            return


        for produto in produtos_planilha:
            resultado = buscar(produto)

            valor = resultado["preco"]
            print(produto, valor)
            

