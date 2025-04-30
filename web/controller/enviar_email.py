import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
import os

# Carrega as variáveis do .env
load_dotenv()
senhaEmail = os.getenv("PASSWORD_EMAIL_APP")

def enviar_email(destinatario, assunto, corpo, anexo_path):
    remetente = "profjpmoraes@gmail.com"
    servidor_smtp = "smtp.gmail.com"
    porta_smtp = 587

    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = assunto
    msg.attach(MIMEText(corpo, 'plain'))

    try:
        with open(anexo_path, "rb") as anexo:
            parte = MIMEBase('application', 'octet-stream')
            parte.set_payload(anexo.read())
            encoders.encode_base64(parte)
            parte.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(anexo_path)}"')
            msg.attach(parte)
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {anexo_path}")
        return

    try:
        with smtplib.SMTP(servidor_smtp, porta_smtp) as servidor:
            servidor.starttls()
            servidor.login(remetente, senhaEmail)
            servidor.sendmail(remetente, destinatario, msg.as_string())
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar o e-mail: {e}")
