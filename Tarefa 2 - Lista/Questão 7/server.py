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
                 

                dataIdade = conn.recv(1024)
                TempoIdade = dataIdade.decode('utf-8')
                TempoIdade = int(TempoIdade)
                
                dataTempoTrabalho = conn.recv(1024)
                TempoTrabalho = dataTempoTrabalho.decode('utf-8')
                TempoTrabalho = int(TempoTrabalho)
               

                if TempoIdade > 65:
                    
                    Aposentar = 'O indivíduo já pode se aposentar'
                    msg = Aposentar.encode('utf-8') 
                    reply = msg
                    conn.sendall(reply)
                
                elif TempoTrabalho > 30:

                    Aposentar = 'O indivíduo já pode se aposentar'
                    msg = Aposentar.encode('utf-8') 
                    reply = msg
                    conn.sendall(reply)

                elif TempoIdade > 60 & TempoTrabalho >25:

                    Aposentar = 'O indivíduo já pode se aposentar'
                    msg = Aposentar.encode('utf-8') 
                    reply = msg
                    conn.sendall(reply)

                else:
                    Aposentar = 'O indivíduo não pode se aposentar'
                    msg = Aposentar.encode('utf-8') 
                    reply = msg
                    conn.sendall(reply)

                exit()
                
			
    finally:
		# Clean up the connection
	    conn.close()