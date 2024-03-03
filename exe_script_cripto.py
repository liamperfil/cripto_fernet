# Executar script interno criptografado
from cryptography.fernet import Fernet

# Receber chave contida em arquivo chave.key
with open('chave.key', 'rb') as resposta:
    chave = resposta.read()

# Suporte
fernet = Fernet(chave)

# Ler o arquivo.txt e salva em conteudo_arquivo
with open('arquivo.txt', 'rb') as resposta:
    conteudo_arquivo = resposta.read()

# Decriptografar, decodificar e executar
conteudo_decode = fernet.decrypt(conteudo_arquivo).decode()
exec(conteudo_decode)