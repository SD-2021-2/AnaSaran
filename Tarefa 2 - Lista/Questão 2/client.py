import socket
import sys

host = 'localhost'
port = 1234

# Cria um socket TCP/IP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

print ('Digite o nome:')
msg = input()
msgNome = bytes(msg, 'utf-8')
s.sendall(msgNome)

print ('\nDigite o sexo (M ou F):')
msg = input()
msgSexo = bytes(msg, 'utf-8')
s.sendall(msgSexo)

print ('\nDigite a idade:\n')
msg = input()
msgIdade = bytes(msg, 'utf-8')
s.sendall(msgIdade)
			


dataMaioridade = s.recv(1014)
dataMaioridade = dataMaioridade.decode('utf-8')
        
dataNome = s.recv(1014)
dataNome = dataNome.decode('utf-8')        
print(dataNome + " " + dataMaioridade)


s.close()