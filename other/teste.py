from dotenv import load_dotenv
import os

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

#Configurar Gemini
senhaEmail = os.getenv("PASSWORD_EMAIL_APP")

print(senhaEmail)

# Limpar variáveis do ambiente
os.environ.clear()