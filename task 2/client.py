import socket

clientSocket = socket.socket()
clientSocket.connect(('localhost', 8888))
S = input()
clientSocket.send(S.encode("utf-8"))

data = clientSocket.recv(1024)
clientSocket.close()

print(data.decode("utf-8"))