import os
import pyaes

# Abrir o arquivo a ser criptografado
file_name = "teste.txt"

# Verifica se o arquivo existe antes de tentar abrir
if os.path.exists(file_name):
    with open(file_name, "rb") as file:
        file_data = file.read()
else:
    print(f"Erro: O arquivo {file_name} não foi encontrado!")
    exit()

# Remover o arquivo original, se existir
os.remove(file_name)

# Definir chave de criptografia
key = b"cc026564cc026564"
aes = pyaes.AESModeOfOperationCTR(key)

# Criptografar os dados do arquivo
crypto_data = aes.encrypt(file_data)

# Salvar o arquivo criptografado
new_file = file_name + ".criptografado"
with open(new_file, 'wb') as new_file_obj:
    new_file_obj.write(crypto_data)

print(f"Arquivo criptografado salvo como {new_file}")
