import openpyxl
import pandas as pd
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
from dateutil.relativedelta import relativedelta
import locale

hoje = datetime.today()
mes_posterior = hoje + relativedelta(months=1)
vencimento = mes_posterior.strftime('%d/%m/%Y')
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
nome_mes = mes_posterior.strftime('%B')

class Planilha:

    def cria_planilha(dicionario):

        dicionario = {
            'Fornecedor' : ['fornecedor1', 'fornecedor2', 'fornecedor3', 'fornecedor4'],
            'Email' : ['angelopiovezan15@gmail.com', 'fornecedor2@email.com', 'fornecedor3@email.com', 'fornecedor4@email.com'],
            'Fornece' : ['Eletronicos', 'Plasticos', 'Maquinas', 'Internet'],
            'Boleto' : ['boleto1', 'boleto2', 'boleto3', 'boleto4']
        }

        nome_planilha = 'dados_fornecedores.xlsx'
        df = pd.DataFrame(dicionario)
        df.to_excel(nome_planilha, index=False)

        print(f"Dados salvos com sucesso em {nome_planilha}")


    def gera_boleto(df):

        df = pd.read_excel('dados_fornecedores.xlsx')

        for index, row in df.iterrows():
            nome    = row['Fornecedor']
            email   = row['Email']
            produto = row['Fornece']
            boleto  = row['Boleto']
            data    = vencimento
            valor   = '$$$$'


            wb = openpyxl.load_workbook('boleto.xlsx')
            ws = wb.active

            ws['B1'] = nome
            ws['B2'] = produto
            ws['B3'] = email
            ws['B4'] = valor
            ws['B5'] = data

            wb.save(f"{boleto}.xlsx")

            print(f"Boleto gerado para {nome}, salvo como {boleto}.xlsx")  


class Email:

    def configura_envia_email(df):

        df = pd.read_excel('dados_fornecedores.xlsx')

        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        email_remetente = "piovezanjorgeto@gmail.com"
        senha = "cwzg gumc ifqx kdls"

        for index, row in df.iterrows():
            
            nome    = row['Fornecedor']
            destino = row['Email']
            boleto  = row['Boleto']
            arquivo   = f'{boleto}.xlsx'

            msg = MIMEMultipart()
            msg['From']    = email_remetente
            msg['To']      = destino
            msg['Subject'] = f'Boleto com vencimento em {mes_posterior}'
            corpo_email    = f'Olá {nome}, segue o boleto com vencimento para {vencimento}.\n\nFavor pagar até a data de vencimento para não haver juros.\n\nAtenciosamente Britânia Eletrodomésticos!'
            msg.attach(MIMEText(corpo_email, "plain"))

            with open(arquivo, "rb") as anexo:
                anexo_bin = MIMEBase("application", "octet-stream")
                anexo_bin.set_payload(anexo.read())
                encoders.encode_base64(anexo_bin)
                anexo_bin.add_header("Content-Disposition", f"atachment; filename={arquivo}")
                msg.attach(anexo_bin)

            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(email_remetente, senha)
                server.sendmail(email_remetente, destino, msg.as_string())
                
            print(f"E-mail enviado para {destino} com o boleto {arquivo}")

    