import socket
import sys

host = 'localhost'
port = 1234

# Cria um socket TCP/IP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

print ('Digite a N1:')
msg = input()
msgNUm = bytes(msg, 'utf-8')
s.sendall(msgNUm)

print ('\nDigite a N2:')
msg = input()
msgNDois = bytes(msg, 'utf-8')
s.sendall(msgNDois)

print ('\nDigite a N3 caso exista\n')
msg = input()
msgNTres = bytes(msg, 'utf-8')
s.sendall(msgNTres)
			


dataAprovacao = s.recv(1014)
dataAprovacao = dataAprovacao.decode('utf-8')
        
print(dataAprovacao)


s.close()