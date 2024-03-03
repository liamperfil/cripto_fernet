# Utilizando Fernet para criptografar/decriptografar
# Salvando o conteúdo em arquivo
from cryptography.fernet import Fernet

# Receber chave contida em arquivo chave.key
with open('chave.key', 'rb') as resposta:
    chave = resposta.read()

# Ler o arquivo.txt e salva em conteudo_arquivo
with open('arquivo.txt', 'rb') as resposta:
    conteudo_arquivo = resposta.read()

# encrypt or decrypt
cripto_decripto = Fernet(chave).encrypt(conteudo_arquivo)

# Escrever no arquivo conteudo criptografado ou decriptografado
with open('arquivo.txt', 'wb') as resposta:
    resposta.write(cripto_decripto)