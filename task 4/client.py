import socket
import threading

clientSocket = socket.socket()
clientSocket.connect(('localhost', 8888))

def accepter():
	while True:
		data = clientSocket.recv(1024)
		print(data.decode("utf-8"))

try:
	my_threard = threading.Thread(target=accepter)
	my_threard.start()
	while True:
		clientSocket.send(input().encode("utf-8"))
except:
	print()
	clientSocket.close()