from socket import *
from cryptography.hazmat.primitives import serialization

class SocketClient:
    def __init__(self):
        self.ip = "127.0.0.1"
        self.port = 8080
    
    def start(self):
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect((self.ip, self.port))

    def stop(self):
        self.client_socket.send("quit".encode("utf-8"))
        self.client_socket.close()

    def get_key(self, option):
        if option == 0:
            self.client_socket.send("public".encode("utf-8"))
            key = serialization.load_pem_public_key(self.client_socket.recv(2048))
        elif option == 1:
            self.client_socket.send("private".encode("utf-8"))
            key = serialization.load_pem_private_key(self.client_socket.recv(2048))
        else:
            self.client_socket.send("quit".encode("utf-8"))

        return key