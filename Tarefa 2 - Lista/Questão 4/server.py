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
            

                dataSexo = conn.recv(1024)
                Sexo = dataSexo.decode('utf-8')
                

                dataAltura = conn.recv(1024)
                Altura = dataAltura.decode('utf-8')
                Altura = float(Altura)

                
                
                if Sexo == 'F':
                    PesoIdeal = (72.7 * Altura)
                    PesoIdeal = PesoIdeal - 58
                    PesoMensagem = str(PesoIdeal)
                    msg = PesoMensagem.encode('utf-8') 
                    reply = msg
                    conn.sendall(reply)
                else:
                    PesoIdeal = (62.1 * Altura)
                    PesoIdeal = PesoIdeal - 44.7
                    PesoMensagem = str(PesoIdeal)
                    msg = PesoMensagem.encode('utf-8')  
                    reply = msg
                    conn.sendall(reply)

                exit()
                
			
    finally:
		# Clean up the connection
	    conn.close()