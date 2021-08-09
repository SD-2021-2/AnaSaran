import socket
import sys

host = 'localhost'
port = 1234

# Cria um socket TCP/IP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))


print ('\nQual o seu saldo médio?\n')
msg = input()
msgSaldoM = bytes(msg, 'utf-8')
s.sendall(msgSaldoM)	

datasaldoM = s.recv(1014)
datasaldoM = datasaldoM.decode('utf-8')

dataCredito = s.recv(1014)
dataCredito = dataCredito.decode('utf-8')
             

print("Seu saldo médio é de " + datasaldoM + " e o seu crédito obtido é de " + dataCredito)



s.close()