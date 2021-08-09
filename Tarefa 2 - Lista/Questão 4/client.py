import socket
import sys

host = 'localhost'
port = 1234

# Cria um socket TCP/IP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))


print ('\nDigite o sexo (M ou F):')
msg = input()
msgSexo = bytes(msg, 'utf-8')
s.sendall(msgSexo)

print ('\nDigite a altura:\n')
msg = input()
msgAltura = bytes(msg, 'utf-8')
s.sendall(msgAltura)
			


dataPesoIdeal = s.recv(1014)
dataPesoIdeal = dataPesoIdeal.decode('utf-8')
             
print("Seu peso ideal é de", dataPesoIdeal)


s.close()