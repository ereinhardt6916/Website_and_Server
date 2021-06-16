import socket

class SocketHelper:

	s = None
	conn = None
	addr = None
	setup_timeout = 20
	receive_timeout = 20

	def __init__(self,host,port):
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.settimeout(20)
		self.s.bind((host, port))
		self.s.listen(5)

	def s_appept(self):
		try:
			self.conn,self.addr = self.s.accept()
		except:
			return("Fset")

	def send_data(self,content):
		try:
			self.conn.send(content)
		except:
			return("Fsnd")


	def read_data(self):
		try:
			self.conn.settimeout(10)
			buf = self.conn.recv(1024)
			return buf
		except:
			return("Frev")

	def close_socket(self):
		self.conn.close()