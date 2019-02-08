from socket import *

HOST = '127.0.0.1'
PORT = 10001
BUFFER = 1024
ADDRESS = (HOST, PORT)

while True:
    tcpClientSocket = socket(AF_INET, SOCK_STREAM)
    tcpClientSocket.connect(ADDRESS)

    data = input('> ')
    if not data:
        break

    tcpClientSocket.send(('%s\r\n' %data).encode())
    data = tcpClientSocket.recv(BUFFER)
    if not data:
        break
    print(data.strip().decode())

tcpClientSocket.close()
