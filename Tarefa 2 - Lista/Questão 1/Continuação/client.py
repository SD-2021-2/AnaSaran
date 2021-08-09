import socket
import sys

host = 'localhost'
port = 1234

# Cria um socket TCP/IP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

print ('Digite o nome do funcionário\n')
msg = input()
msgNome = bytes(msg, 'utf-8')
s.sendall(msgNome)

print ('Digite o salário do funcionário\n')
msg = input()
msgSalario = bytes(msg, 'utf-8')
s.sendall(msgSalario)

print ('Digite o cargo\n')
msg = input()
msgCargo = bytes(msg, 'utf-8')
s.sendall(msgCargo)
			
dataSalario = s.recv(1014)
dataSalario = dataSalario.decode('utf-8')

dataNome = s.recv(1024)
dataNome = dataNome.decode('utf-8')
        
print("\n\nNome do colaborador", dataNome)
print("Salário reajustado", dataSalario)


s.close()