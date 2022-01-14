import socket
import threading

serverSocket = socket.socket()
serverSocket.bind(('localhost', 8888))
serverSocket.listen(100)

connections = []

def conn_proccess(conn):
	while True:
		try:
			data = conn.recv(1024)
			for c in connections:
				if c != conn:
					try:
						c.send(data)
					except:
						if c in connections:
							connections.remove(c)
		except:
			if conn in connections:
				connections.remove(conn)

while True:
	conn, addr = serverSocket.accept()
	connections.append(conn)
	my_threard = threading.Thread(target=conn_proccess, args=[conn])
	my_threard.start()