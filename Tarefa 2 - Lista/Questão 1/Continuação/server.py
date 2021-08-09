import socket
import sys
import struct

# Significa que é possível receber conexões fora da rede local
host = ''

port = 1234

# Cria um socket TCP/IP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#garante que o socket será destruído (pode ser reusado) após uma interrupção da execução 
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
# associa o socket a porta
s.bind((host, port))

print('Server %s on port %s' % (socket.gethostname(), port))


# Enfileira uma nova conexão,  (define o modo servidor)
s.listen(8)

while True:
     # Espera por novas conexões
    print('waiting for a connection')
        
    # Aceita conexões
    conn, address = s.accept()

    

    try:

	    while True:

                dataNome = conn.recv(1024)

                dataSalario = conn.recv(1024)

                dataCargo = conn.recv(1014)

                dataCargo = dataCargo.decode('utf-8')
                print(dataCargo)
                
                if dataCargo == 'operador':

                    SalarioSemReajuste = dataSalario.decode('utf-8')
                    SalarioSemReajuste = float(SalarioSemReajuste)
                    SalarioReajustado = SalarioSemReajuste * 1.2
                    SalarioReajustado = str(SalarioReajustado)
                    print(SalarioReajustado)
                    dataSalario = SalarioReajustado.encode('utf-8') 
                    reply = dataSalario
                    conn.sendall(reply)

                else:
                    if dataCargo == 'programador':
                        SalarioSemReajuste = dataSalario.decode('utf-8')
                        SalarioSemReajuste = float(SalarioSemReajuste)
                        SalarioReajustado = SalarioSemReajuste * 1.18
                        SalarioReajustado = str(SalarioReajustado)
                        print(SalarioReajustado)
                        dataSalario = SalarioReajustado.encode('utf-8') 
                        reply = dataSalario
                        conn.sendall(reply)
               

                reply = dataNome
                conn.sendall(reply)

                exit()
                
			
    finally:
		# Clean up the connection
	    conn.close()