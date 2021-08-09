import socket
import sys

host = 'localhost'
port = 1234

# Cria um socket TCP/IP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))


print ('\nQual é o seu nome?\n')
msg = input()
msgNome = bytes(msg, 'utf-8')
s.sendall(msgNome)

print ('\nQual é o seu nível?\n')
msg = input()
msgNível = bytes(msg, 'utf-8')
s.sendall(msgNível)		

print ('\nQual é o seu salário?\n')
msg = input()
msgSalario = bytes(msg, 'utf-8')
s.sendall(msgSalario)	

print ('\nQuantos dependentes você tem?\n')
msg = input()
msgDependentes = bytes(msg, 'utf-8')
s.sendall(msgDependentes)	


dataNome = s.recv(1014)
dataNome = dataNome.decode('utf-8')

dataCategoria = s.recv(1014)
dataCategoria = dataCategoria.decode('utf-8')

dataNivel = s.recv(1014)
dataNivel = dataNivel.decode('utf-8')
             
print("Seu nome é "+ dataNome)
print("seu nível é "+ dataNivel)
print("e seu salário é " + dataCategoria)


s.close()