
import socket
import sys

# IP, PORT AND BUFFERSIZE CONNECTION
SRV_ADDR = ('192.168.10.1')
PORT = 7
BUFF_SIZE = 64

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Open socket on {} port {}'.format(SRV_ADDR,PORT))
sock.bind((SRV_ADDR,PORT))

# Listen for incoming connections
sock.listen(5)

while True:
    # Wait a client connection
    print('Waiting for a connection')
    connection, cli_addr = sock.accept()
    try:
        print('Connection receive from',cli_addr)
        # Receive the data and retransmit it
        while True:
            data = connection.recv(BUFF_SIZE)
            print('received {}'.format(data))
            if data:
                print('return data to the client..')
                connection.sendall(data)
            else:
                print('no data from client')
                break

    finally:
        #It ensures that the port is closed
        connection.close()