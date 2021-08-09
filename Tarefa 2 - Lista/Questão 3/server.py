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

                dataNUm = conn.recv(1024)
                NUm = dataNUm.decode('utf-8')
                NUm = float(NUm)

                dataNDois = conn.recv(1024)
                NDois = dataNDois.decode('utf-8')
                NDois = float(NDois)

                dataNTres = conn.recv(1014)
                NTres = dataNTres.decode('utf-8')
                NTres = float(NTres)
                
                
                M = NUm + NDois
                M = M/2

                if M > 7:

                    mensagem = 'Aluno aprovado'
                    msg = mensagem.encode('utf-8') 
                    reply = msg
                    conn.sendall(reply)
                    
                else:
                    if M < 3:
                        mensagem = 'Aluno reprovado'
                        msg = mensagem.encode('utf-8') 
                        reply = msg
                        conn.sendall(reply)
                    else:
                        M = M + NTres
                        M = M/2

                        if M > 5:
                            mensagem = 'Aprovado'
                            msg = mensagem.encode('utf-8') 
                            reply = msg
                            conn.sendall(reply)
                        else:
                            mensagem = 'Reprovado'
                            msg = mensagem.encode('utf-8') 
                            reply = msg
                            conn.sendall(reply)
                            

            exit()
                
			
    finally:
		# Clean up the connection
	    conn.close()