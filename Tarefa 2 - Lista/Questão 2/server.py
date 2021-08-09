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
                

                dataSexo = conn.recv(1024)
                Sexo = dataSexo.decode('utf-8')
                

                dataIdade = conn.recv(1024)
                Idade = dataIdade.decode('utf-8')
                Idade = int(Idade)

                
                
                if Sexo == 'F':
                    if Idade > 21:

                        mensagem = 'atingiu a maioridade'
                        msg = mensagem.encode('utf-8') 
                        reply = msg
                        conn.sendall(reply)

                    else:
                        mensagem = 'não atingiu a maioridade'
                        msg = mensagem.encode('utf-8') 
                        reply = msg
                        conn.sendall(reply)
                else:

                    if Idade > 18:

                        mensagem = 'atingiu a maioridade'
                        msg = mensagem.encode('utf-8') 
                        reply = msg
                        conn.sendall(reply)

                    else:

                        mensagem = 'não atingiu a maioridade'
                        msg = mensagem.encode('utf-8') 
                        reply = msg
                        conn.sendall(reply)
                            

                reply = dataNome
                conn.sendall(reply)

                exit()
                
			
    finally:
		# Clean up the connection
	    conn.close()