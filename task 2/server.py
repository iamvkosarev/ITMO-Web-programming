import socket

serverSocket = socket.socket()
serverSocket.bind(('localhost', 8888))
serverSocket.listen()

while True:
	conn, addr = serverSocket.accept()
	data = conn.recv(1024)
	S = data.decode('utf-8')
	a, h = map(float, S.split())
	x = str(a * h)

	conn.send(x.encode("utf-8"))