import socket
import sys

host = 'localhost'
port = 1234

# Cria um socket TCP/IP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))


print ('\nQual a idade?\n')
msg = input()
msgIdade = bytes(msg, 'utf-8')
s.sendall(msgIdade)
			


dataCategoria = s.recv(1014)
dataCategoria = dataCategoria.decode('utf-8')
             
print("Sua classificação é", dataCategoria)


s.close()