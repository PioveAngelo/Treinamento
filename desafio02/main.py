import pandas as pd
import config


def main():
    '''
        Função somente para as chamadas dos métodos setados no arquivo config.py
    '''
    dicionario = {
                'Fornecedor' : ['fornecedor1', 'fornecedor2', 'fornecedor3', 'fornecedor4'],
                'Email' : ['angelopiovezan15@gmail.com', 'fornecedor2@email.com', 'fornecedor3@email.com', 'fornecedor4@email.com'],
                'Fornece' : ['Eletronicos', 'Plasticos', 'Maquinas', 'Internet'],
                'Boleto' : ['boleto1', 'boleto2', 'boleto3', 'boleto4']
            }

    config.Planilha.cria_planilha(dicionario)

    df = pd.read_excel('dados_fornecedores.xlsx')

    config.Planilha.gera_boleto(df)

    config.Email.configura_envia_email(df)


if __name__ == "__main__":
    main()
    print("Operação feita com sucesso!")