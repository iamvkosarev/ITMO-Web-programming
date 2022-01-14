import socket

serverSocket = socket.socket()
serverSocket.bind(('localhost', 8888))
serverSocket.listen()

while True:
	conn, addr = serverSocket.accept()
	data = conn.recv(1024)
	body = open('index.html').read()
	print(body)
	S = 'HTTP/1.1 200 OK\n'
	S += 'Content-Type: text/html; charset=utf-8\n'
	S += 'Content-Length: ' + str(len(body)) + '\n\n'
	S += body
	conn.send(S.encode("utf-8"))