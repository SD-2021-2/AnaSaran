import socket
import sys

host = 'localhost'
port = 1234

# Cria um socket TCP/IP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))


print ('\nQual a sua idade??\n')
msg = input()
msgIdade = bytes(msg, 'utf-8')
s.sendall(msgIdade)

print ('\nQual o seu tempo de serviço?\n')
msg = input()
msgServico = bytes(msg, 'utf-8')
s.sendall(msgServico)	

dataPodeAposentar = s.recv(1014)
dataPodeAposentar = dataPodeAposentar.decode('utf-8')
             

print(dataPodeAposentar)



s.close()