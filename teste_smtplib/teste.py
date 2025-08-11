import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configurações do servidor SMTP

smtp_server = "smtp.gmail.com"
smtp_port = 587
email_remetente = "piovezanjorgeto@gmail.com"
senha = "cwzg gumc ifqx kdls"

# Configuração do E-mail

email_destinatario = "angelopiovezan15@gmail.com"
assunto = "Teste"
mensagem = "Esse é um e-mail enviado usando smtplib em python"

# Criando o E-mail

email = MIMEMultipart()
email["From"] = email_remetente
email["To"] = email_destinatario
email["Subject"] = assunto
email.attach(MIMEText(mensagem, "plain"))


try:
    # Conexão com o servidor SMTP

    servidor = smtplib.SMTP(smtp_server, smtp_port)
    servidor.starttls() # Inicia a conexão segura (TLS)
    servidor.login(email_remetente, senha) # Autenticação
    servidor.sendmail(email_remetente, email_destinatario, email.as_string()) # Envia o E-mail

    print("E-mail enviado com sucesso!")

except Exception as e:
    print(f"Erro ao enviar e-mail: {e}")

finally:
    servidor.quit() # Encerra a conexão
