import os
from dotenv import load_dotenv

# Carga variables de entorno desde .env
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Más adelante aquí podríamos meter clases tipo Settings, otras keys, etc.