import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
import os

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

#Configurar Gemini
senhaEmail = os.getenv("PASSWORD_EMAIL")

def enviar_email(destinatario, assunto, corpo, anexo_path):
    # Configurações do servidor SMTP do Gmail
    remetente = "seu_email@gmail.com"
    senha = senhaEmail
    servidor_smtp = "smtp.gmail.com"
    porta_smtp = 587

    # Criar o objeto do e-mail
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = assunto

    # Adicionar o corpo do e-mail
    msg.attach(corpo)

    # Adicionar o anexo
    anexo = open(anexo_path, "rb")  # Abrir o arquivo em modo binário
    parte = MIMEBase('application', 'octet-stream')
    parte.set_payload(anexo.read())
    encoders.encode_base64(parte)  # Codifica o arquivo em base64
    parte.add_header('Content-Disposition', f"attachment; filename={anexo_path}")
    msg.attach(parte)

    # Conectar ao servidor SMTP e enviar o e-mail
    try:
        servidor = smtplib.SMTP(servidor_smtp, porta_smtp)
        servidor.starttls()  # Encripta a conexão
        servidor.login(remetente, senha)
        texto = msg.as_string()
        servidor.sendmail(remetente, destinatario, texto)
        servidor.quit()
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar o e-mail: {e}")


# Exemplo de uso
def main():
    # Defina o destinatário, assunto e corpo do e-mail
    destinatario = "destinatario@example.com"
    assunto = "Documentos Gerados"
    corpo = "Olá, segue o documento gerado em anexo."
    
    # Caminho do anexo
    anexo_path = "resultado.pdf"
    
    # Enviar e-mail com o anexo
    enviar_email(destinatario, assunto, corpo, anexo_path)

if __name__ == "__main__":
    main()
