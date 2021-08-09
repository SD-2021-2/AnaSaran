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
                 

                dataSaldoM = conn.recv(1024)
                msg = dataSaldoM
                reply = msg
                conn.sendall(reply)

                SaldoM = dataSaldoM.decode('utf-8')
                SaldoM = float(SaldoM)
            

                if 0 < SaldoM < 200.0:
                    
                    Credito = '0 créditos'
                    msg = Credito.encode('utf-8') 
                    reply = msg
                    conn.sendall(reply)
                
                elif 201.0 < SaldoM < 400.0:

                    CreditoValor = SaldoM * 0.2
                    CreditoValor = str(CreditoValor)
                    Credito = CreditoValor + ' créditos'
                    msg = Credito.encode('utf-8') 
                    reply = msg
                    conn.sendall(reply)

                elif 401.0 < SaldoM < 600.0:

                    CreditoValor = SaldoM * 0.3
                    CreditoValor = str(CreditoValor)
                    Credito = CreditoValor + ' créditos'
                    msg = Credito.encode('utf-8') 
                    reply = msg
                    conn.sendall(reply)

                elif SaldoM > 601.0:

                    CreditoValor = SaldoM * 0.4
                    CreditoValor = str(CreditoValor)
                    Credito = CreditoValor + ' créditos'
                    msg = Credito.encode('utf-8') 
                    reply = msg
                    conn.sendall(reply)

                exit()
                
			
    finally:
		# Clean up the connection
	    conn.close()