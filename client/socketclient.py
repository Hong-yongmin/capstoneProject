from socket import *

class SocketClient:
    def __init__(self):
        self.ip = "127.0.0.1"
        self.port = 8080
    
    def start(self):
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect((self.ip, self.port))

        self.client_socket.send("public".encode("utf-8"))

        self.data = self.client_socket.recv(1024)

        print("public key : " + self.data.decode("utf-8"))

        self.client_socket.send("quit".encode("utf-8"))

        self.client_socket.close()