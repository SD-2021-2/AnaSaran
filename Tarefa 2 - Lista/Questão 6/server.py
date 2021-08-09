import socket
import sys
import struct
import time

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

                msg = dataNome
                reply = msg
                conn.sendall(reply) 
                

                dataNivel = conn.recv(1024)
                Nivel = dataNivel.decode('utf-8')

                dataSalario = conn.recv(1024)
                Salario = dataSalario.decode('utf-8')
                Salario = float(Salario)

                dataDependentes= conn.recv(1024)
                Dependentes = dataDependentes.decode('utf-8')
                Dependentes = int(Dependentes)


                if Nivel == 'A':
                    if Dependentes > 0:
                        Salario = Salario * 0.92
                    else:
                        Salario = Salario * 0.97

                    Salario = str(Salario)
                    msg = Salario.encode('utf-8') 
                    reply = msg
                    conn.sendall(reply)
                
                elif Nivel == 'B':

                    if Dependentes > 0:
                        Salario = Salario * 0.9
                    else:
                        Salario = Salario * 0.95

                    Salario = str(Salario)
                    msg = Salario.encode('utf-8') 
                    reply = msg
                    conn.sendall(reply)

                elif Nivel == 'C':

                    if Dependentes > 0:
                        Salario = Salario * 0.85
                    else:
                        Salario = Salario * 0.92

                    Salario = str(Salario)
                    msg = Salario.encode('utf-8') 
                    reply = msg
                    conn.sendall(reply)

                elif Nivel == 'D':

                    if Dependentes > 0:
                        Salario = Salario * 0.83
                    else:
                        Salario = Salario * 0.90

                    Salario = str(Salario)
                    msg = Salario.encode('utf-8') 
                    reply = msg
                    conn.sendall(reply)
 
               
                time.sleep(1) 
                msg = dataNivel
                reply = msg
                conn.sendall(reply)

                exit()
                
			
    finally:
		# Clean up the connection
	    conn.close()