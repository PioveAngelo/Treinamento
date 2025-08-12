import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

df = pd.read_excel('dados_clientes.xlsx')

# Configurar o servidor SMTP

smtp_server = "smtp.gmail.com"
smtp_port = 587
email_remetente = "piovezanjorgeto@gmail.com"
senha = "cwzg gumc ifqx kdls"

# Configuração do E-mail

for index, row in df.iterrows():
    nome = row['Nome']
    email_destino = row['Email']
    arquivo_nota = f'nota_{nome}.xlsx'

    msg = MIMEMultipart()
    msg["From"] = email_remetente
    msg["To"] = email_destino
    msg["Subject"] = "Sua Nota Fiscal"
    corpo_email = f"Olá {nome},\n\nSegue em anexo a sua nota fiscal.\n\nAtenciosamente,\nEmpresa XYZ"
    msg.attach(MIMEText(corpo_email, "plain"))

    # Anexar a nota fiscal

    with open(arquivo_nota, "rb") as anexo:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(anexo.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename={arquivo_nota}")
        msg.attach(part)

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(email_remetente, senha)
        server.sendmail(email_remetente, email_destino, msg.as_string())
    
    print(f"E-mail enviado para {nome} ({email_destino}) com a nota fiscal '{arquivo_nota}'")

print("Todos os e-mails foram enviados com sucesso.")
